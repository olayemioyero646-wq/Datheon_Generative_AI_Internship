from pathlib import Path
import ast
import operator
from ddgs import DDGS
from dotenv import load_dotenv
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
import os



@tool
def read_local_file(file_path: str) -> str:
    """Read the contents of a local text file."""

    path = Path(file_path)

    if not path.is_file():
        return f"Error: File not found: {file_path}"

    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return "Error: This file is not a readable UTF-8 text file."
    except OSError as error:
        return f"Error reading file: {error}"


@tool
def calculate(expression: str) -> str:
    """Safely calculate a mathematical expression using basic arithmetic."""

    operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.FloorDiv: operator.floordiv,
        ast.Mod: operator.mod,
        ast.Pow: operator.pow,
        ast.USub: operator.neg,
        ast.UAdd: operator.pos,
    }

    def evaluate(node):
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value

        if isinstance(node, ast.BinOp) and type(node.op) in operators:
            left = evaluate(node.left)
            right = evaluate(node.right)

            if isinstance(node.op, ast.Pow) and abs(right) > 1000:
                raise ValueError("Exponent is too large.")

            result = operators[type(node.op)](left, right)

            if isinstance(result, (int, float)) and abs(result) > 1e100:
                raise ValueError("Result is too large.")

            return result

        if isinstance(node, ast.UnaryOp) and type(node.op) in operators:
            return operators[type(node.op)](evaluate(node.operand))

        raise ValueError("Unsupported mathematical expression.")

    try:
        tree = ast.parse(expression, mode="eval")
        result = evaluate(tree.body)
        return str(result)

    except (ValueError, TypeError, ZeroDivisionError, OverflowError, SyntaxError) as error:
        return f"Calculation error: {error}"



@tool
def web_search(query: str) -> str:
    """Search the web using DuckDuckGo and return relevant search results."""

    try:
        results = DDGS().text(query, max_results=5)

        if not results:
            return "No search results were found."

        formatted_results = []

        for index, result in enumerate(results, start=1):
            title = result.get("title", "No title")
            body = result.get("body", "No description")
            url = result.get("href", "No URL")

            formatted_results.append(
                f"{index}. {title}\n"
                f"Description: {body}\n"
                f"URL: {url}"
            )

        return "\n\n".join(formatted_results)

    except Exception as error:
        return f"Web search failed: {error}"
    
# Load environment variables from the Task 3 .env file
load_dotenv(Path(__file__).parent / ".env")

# Configure the Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-3.7-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0,
)

# Register all available tools

tools = [read_local_file, calculate, web_search]

# Create the autonomous AI agent

agent = create_agent(
model=llm,
tools=tools,
system_prompt=(
"You are a helpful multi-tool AI assistant. "
"Use the web search tool when current or external information is needed. "
"Use the calculator tool for mathematical calculations. "
"Use the local file reader when asked to inspect a local text file. "
"You may use multiple tools to answer a question. "
"Never claim to have used a tool if you did not actually use it. "
"Explain your findings clearly and accurately."
),
)
# Run the agent interactively

if __name__ == "__main__":
    print("\nMulti-Tool Autonomous AI Agent")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in {"exit", "quit"}:
            print("Agent: Goodbye!")
            break

        if not user_input:
            continue

        try:
            response = agent.invoke(
                {"messages": [{"role": "user", "content": user_input}]}
            )

            final_message = response["messages"][-1]
            content = final_message.content

            if isinstance(content, list):
                text_parts = [
                    block["text"]
                    for block in content
                    if isinstance(block, dict)
                    and block.get("type") == "text"
                    and block.get("text")
                ]
                display_text = "\n".join(text_parts)
            else:
                display_text = str(content)

            print(f"\nAgent: {display_text}\n")

        except Exception as error:
            print(f"\nAgent error: {error}\n")