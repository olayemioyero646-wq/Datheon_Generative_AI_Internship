
import os
import tempfile

import streamlit as st
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

st.set_page_config(
    page_title="Document Q&A Assistant",
    page_icon="📚",
    layout="wide",
)

st.title("📚 Document Q&A Assistant")
st.write(
    "Upload a PDF, then ask questions about its contents. "
    "Answers are generated using information retrieved from your document."
)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error(
        "GEMINI_API_KEY was not found. "
        "Please check that your API key is configured in the project's root .env file."
    )
    st.stop()

uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])

if uploaded_file is not None:
    if st.button("Process Document"):
        with st.spinner("Reading and processing your document..."):
            try:
                with tempfile.NamedTemporaryFile(
                    delete=False, suffix=".pdf"
                ) as temp_file:
                    temp_file.write(uploaded_file.getvalue())
                    temp_path = temp_file.name

                try:
                    loader = PyPDFLoader(temp_path)
                    documents = loader.load()
                finally:
                    os.remove(temp_path)

                if not documents:
                    st.error("No readable text was found in this PDF.")
                    st.stop()

                splitter = RecursiveCharacterTextSplitter(
                    chunk_size=1000,
                    chunk_overlap=150,
                )
                chunks = splitter.split_documents(documents)

                embeddings = GoogleGenerativeAIEmbeddings(
                    model="models/gemini-embedding-001",
                    google_api_key=api_key,
                )

                vector_store = Chroma.from_documents(
                    documents=chunks,
                    embedding=embeddings,
                )

                st.session_state["vector_store"] = vector_store
                st.session_state["document_name"] = uploaded_file.name

                st.success(
                    f"Processed {uploaded_file.name} successfully. "
                    f"Created {len(chunks)} text chunks."
                )

            except Exception as error:
                st.error(f"Document processing failed: {error}")

if "vector_store" in st.session_state:
    st.subheader("Ask a question")

    question = st.text_input(
        "Enter your question about the uploaded document:"
    )

    if st.button("Get Answer"):
        if not question.strip():
            st.warning("Please enter a question first.")
        else:
            with st.spinner("Searching the document and generating an answer..."):
                try:
                    vector_store = st.session_state["vector_store"]
                    relevant_docs = vector_store.similarity_search(
                        question,
                        k=4,
                    )

                    context = "\n\n".join(
                        f"Page {doc.metadata.get('page', 0) + 1}:\n{doc.page_content}"
                        for doc in relevant_docs
                    )

                    prompt = ChatPromptTemplate.from_messages(
                        [
                            (
                                "system",
                                "Answer the user's question using only the "
                                "provided document context. If the answer is "
                                "not contained in the context, say you could "
                                "not find the answer in the document. "
                                "Do not invent facts.",
                            ),
                            (
                                "human",
                                "Document context:\n{context}\n\n"
                                "Question: {question}",
                            ),
                        ]
                    )

                    llm = ChatGoogleGenerativeAI(
                        model="gemini-3.8-flash",
                        google_api_key=api_key,
                        temperature=0,
                    )

                    chain = prompt | llm
                    response = chain.invoke(
                        {
                            "context": context,
                            "question": question,
                        }
                    )

                    st.markdown("### Answer")

                    answer = response.content

                    if isinstance(answer, list):
                        answer = "\n".join(
                            item.get("text", "")
                            for item in answer
                            if isinstance(item, dict)
                            and item.get("type") == "text"
                        )

                    st.markdown(answer)
                    for doc in relevant_docs:
                        page_number = doc.metadata.get("page", 0) + 1
                        with st.expander(f"Page {page_number}"):
                            st.write(doc.page_content)

                except Exception as error:
                    st.error(f"Could not answer the question: {error}")