## Document Q&A Assistant

A Retrieval-Augmented Generation (RAG) application developed as part of the Datheon Python, Generative AI, and LangChain Internship.

The application allows users to upload PDF documents and ask questions about their contents. It retrieves relevant passages from the uploaded document and uses Google's Gemini model to generate context-based answers.

## Features

* Upload PDF documents through a web interface.
* Extract text from PDF documents.
* Split document text into smaller chunks.
* Generate vector embeddings using Google's Gemini embedding model.
* Store document embeddings in ChromaDB.
* Retrieve relevant document passages using similarity search.
* Generate answers using a Gemini language model.
* Display retrieved passages as supporting sources.
* Instruct the model to acknowledge when requested information cannot be found in the retrieved context.

## Technologies Used

* Python
* Streamlit
* LangChain
* Google Gemini API
* ChromaDB
* PyPDF
* python-dotenv

## Project Structure

```text
task2_document_qa/
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
```

The Gemini API key is stored in a local `.env` file and must not be committed to GitHub.

## Prerequisites

* Python installed on your computer.
* A Google Gemini API key.
* Internet access for Gemini API requests.

## Installation

1. Open a terminal in the main internship project directory.
2. Activate the existing virtual environment if you have one.
3. Install the required dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

   Run this command from the directory containing the relevant `requirements.txt` file.

## API Configuration

Create a `.env` file in the main project directory and add your Gemini API key:

```text
GEMINI_API_KEY=your_actual_api_key
```

Replace the placeholder with your own API key. Do not share the key or commit the `.env` file to version control.

## Running the Application

From the main internship project directory, run:

```powershell
python -m streamlit run task2_document_qa/app.py
```

Streamlit will provide a local address where you can open the application in your browser.

## How to Use

1. Open the application.
2. Upload a PDF document.
3. Click **Process Document**.
4. Wait for the document to be extracted, split into chunks, embedded, and stored in ChromaDB.
5. Enter a question about the document.
6. Click **Get Answer**.
7. Review the generated answer and the retrieved source passages.

## Testing

The application was tested with a one-page CV.

Example question:

**Question:** What technical skills are listed in this CV?

**Result:** The application retrieved and returned the technical skills listed under the CV's Core Competencies section.

A second test asked for the applicant's monthly salary. Because the supplied document did not contain that information, the application reported that it could not find the answer in the document.

These tests demonstrate the basic document retrieval and question-answering workflow. They do not guarantee that every response will be accurate.

## Limitations

* Processing large documents may exceed the Gemini API's free-tier embedding quota.
* Successful operation depends on API availability, quota limits, and network connectivity.
* Answer quality depends on the text extracted from the PDF and the relevance of retrieved passages.
* Scanned PDFs may require OCR if they do not contain extractable text.
* The application is a learning project and has not been designed as a production-grade document management system.

## Internship Context

This project was developed as part of the Datheon Python, Generative AI, and LangChain Internship. It demonstrates practical use of document processing, text chunking, vector embeddings, similarity search, and retrieval-augmented question answering.