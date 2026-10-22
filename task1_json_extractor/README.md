# Structured LLM Prompt Pipeline & JSON Extractor

## Overview

This project is a structured information extraction tool built with Python, Google's Gemini API, and Pydantic.

It accepts unstructured text, such as a resume or professional profile, and extracts key information into a structured JSON format.

## Features

* **LLM Integration:** Uses Google's Gemini API to extract information from text.
* **Structured Output:** Returns information in JSON format.
* **Data Validation:** Uses Pydantic to validate the extracted information.
* **Custom Input:** Allows users to enter their own resume or profile text.
* **Automatic Retries:** Retries failed API requests up to three times.
* **Error Handling:** Reports extraction errors and handles empty input.

## Information Extracted

The application extracts three fields:

| Field              | Description                      | Example             |
| ------------------ | -------------------------------- | ------------------- |
| `name`             | Person's full name               | Michael James       |
| `skills`           | List of professional skills      | Python, SQL, Docker |
| `experience_years` | Years of professional experience | 5                   |

## Technologies Used

* Python
* Google Gemini API
* Google Gen AI SDK
* Pydantic
* python-dotenv

## Project Structure

```text
task1_json_extractor/
├── main.py
└── README.md
```

The main project's `.env` file stores the API key and should remain outside version control.

## Requirements

* Python 3.10 or later
* A Google Gemini API key
* Internet access

## Installation

### 1. Install the dependencies

From the main project directory, run:

```bash
pip install google-genai pydantic python-dotenv
```

### 2. Configure the API key

Create a `.env` file in the main project directory, one level above `task1_json_extractor`.

Add the following line, replacing the placeholder with your own API key:

```text
GEMINI_API_KEY=your_actual_api_key
```

Keep your API key private. Do not upload the `.env` file to GitHub.

### 3. Run the application

From the main project directory, execute:

```bash
python task1_json_extractor/main.py
```

### 4. Enter the text

Enter the resume or profile text, pressing Enter after each line.

Type `END` on a new line to finish your input.

The application will process the text and display the extracted information as JSON.

## Example

### Input

```text
My name is Michael James.
I have 5 years of experience in software development.
My skills include Python, SQL, Docker, and cloud computing.
END
```

### Output

```json
{
  "name": "Michael James",
  "skills": [
    "Python",
    "SQL",
    "Docker",
    "cloud computing"
  ],
  "experience_years": 5
}
```

## Learning Outcomes

This project demonstrates practical experience with:

* Integrating a large language model through an API.
* Designing prompts for structured information extraction.
* Defining data schemas with Pydantic.
* Validating LLM-generated JSON.
* Managing API credentials using environment variables.
* Implementing basic retries and error handling.
* Accepting user input through a Python command-line application.

## Future Improvements

* Support PDF and DOCX resume uploads.
* Improve retry handling for temporary API errors.
* Add unit tests for input validation and extraction.
* Add a graphical user interface or web API.

## Internship Project

Developed as part of the **Python + Generative AI & LangChain Internship** at Datheon.
