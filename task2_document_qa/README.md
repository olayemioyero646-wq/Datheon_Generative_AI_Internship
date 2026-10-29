# Task 2 — Document Q&A Assistant

## Overview

The Document Q&A Assistant is a Generative AI application that allows users to upload a PDF document and ask questions about its contents. It uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from the document and generate answers.

## Features

* Upload PDF documents.
* Extract text from uploaded PDFs.
* Split document text into manageable chunks.
* Generate embeddings for document retrieval.
* Store document embeddings in ChromaDB.
* Retrieve relevant document sections for a question.
* Generate answers using Google's Gemini model.
* Display retrieved source sections.
* Indicate when the answer cannot be found in the document.

## Technologies Used

* Python
* Streamlit
* LangChain
* Google Gemini API
* ChromaDB
* PyPDF

## Project Structure

```text
task2_document_qa/
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
```

The `.env` file stores the Gemini API key locally and must not be uploaded to GitHub.

## Prerequisites

* Python 3.10 or a compatible version.
* A Google Gemini API key.
* Required Python packages installed.

## Installation

From the main internship project directory, activate the virtual environment if it is not already active:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the Task 2 dependencies:

```powershell
pip install -r task2_document_qa/requirements.txt
```

## API Configuration

Create a `.env` file inside `task2_document_qa` and add your own Gemini API key:

```text
GEMINI_API_KEY=your_gemini_api_key
```

Replace the placeholder with your actual key. Never publish the key or commit the `.env` file to GitHub.

## Running the Application

From the main internship project directory, run:

```powershell
python -m streamlit run task2_document_qa/app.py
```

Streamlit will open the application in your browser.

## How to Use

1. Open the application.
2. Upload a PDF document.
3. Wait for the document to be processed.
4. Enter a question about the document.
5. Review the generated answer and retrieved sources.

## Testing

The application was tested using a CV PDF.

**Test 1: Question answered from the document**

Question: What technical skills are listed in this CV?

Result: The application returned the technical skills listed in the CV, including Python, SQL (DBeaver), VS Code, GitHub, and Git workflow pipelines.

**Test 2: Question not answered by the document**

Question: What is the applicant's monthly salary?

Result: The application indicated that the document did not contain the requested salary information.

These tests demonstrate the application's basic document retrieval and question-answering workflow. More testing is required to assess accuracy across different document types.

## Limitations

* PDF quality and text extraction can affect results.
* API rate limits may restrict document processing.
* Large documents may require additional processing time.
* Generated answers should be checked against the original document.

## Internship Context

This project was developed as Task 2 of the Datheon Python + Generative AI & LangChain Internship.