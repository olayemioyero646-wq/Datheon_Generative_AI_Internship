# Task 3: Multi-Tool Autonomous AI Agent

## Project Overview

This project implements a multi-tool autonomous AI agent using Python, LangChain, and Google's Gemini 3.7 Flash model.

The agent can understand user instructions, select appropriate tools, execute tasks, and provide responses based on the results.

## Features

The agent has three integrated tools:

1. **Local File Reader:** Reads and retrieves the contents of local text files.
2. **Calculator:** Performs mathematical calculations using supported arithmetic operations.
3. **Web Search:** Searches the internet and retrieves relevant information.

## Technologies Used

* Python
* LangChain
* Google Gemini 3.7 Flash
* Google GenAI
* DuckDuckGo Search (DDGS)
* Python-dotenv
* Pydantic

## Project Structure

```text
task3_multi_tool_agent/
│
├── main.py
├── requirements.txt
├── sample.txt
├── README.md
└── .env
```

The `.env` file contains the Gemini API key and must not be uploaded to GitHub.

## Installation and Setup

1. Clone the repository.
2. Navigate to the project directory.
3. Install the required dependencies:

```bash
pip install -r task3_multi_tool_agent/requirements.txt
```

4. Create a `.env` file inside the `task3_multi_tool_agent` folder.
5. Add your Gemini API key:

```text
GEMINI_API_KEY=your_api_key_here
```

6. Run the application from the repository root:

```bash
python task3_multi_tool_agent/main.py
```

## Usage

When the application starts, enter a request at the `You:` prompt.

Examples:

**Calculator**

```text
What is 125 multiplied by 48?
```

**Local File Reader**

```text
Read task3_multi_tool_agent/sample.txt
```

**Web Search**

```text
Search the web for recent developments in artificial intelligence.
```

To close the application, type:

```text
exit
```

## Security

API credentials are stored in a local `.env` file. The file is excluded from version control to prevent accidental exposure of sensitive information.

## Project Objective

The objective of this project is to demonstrate how an AI agent can integrate multiple tools to perform different tasks through natural-language instructions.
