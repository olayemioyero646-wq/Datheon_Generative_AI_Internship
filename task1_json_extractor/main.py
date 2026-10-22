import os
import time
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel, Field


# Find the main project folder and load the API key
PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is missing. Check the .env file in the main project folder."
    )

client = genai.Client(api_key=API_KEY)


# Define the structure of the information to extract
class ExtractedInformation(BaseModel):
    name: str = Field(description="The person's full name")
    skills: list[str] = Field(description="The person's skills")
    experience_years: int = Field(description="Years of experience")


# Extract structured information using Gemini
def extract_information(text: str) -> ExtractedInformation:
    prompt = f"""
Extract the following information from the text:
- Person's full name
- Skills
- Years of experience

Return only information supported by the text.
If years of experience are not stated, use 0.

Text:
{text}
"""

    max_attempts = 3

    for attempt in range(max_attempts):
        try:
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt,
                config={
                    "response_mime_type": "application/json",
                    "response_schema": ExtractedInformation,
                },
            )

            return ExtractedInformation.model_validate_json(response.text)

        except Exception as error:
            if attempt == max_attempts - 1:
                raise

            print(f"Attempt {attempt + 1} failed: {error}")
            print("Retrying in 2 seconds...")
            time.sleep(2)


# Test the extractor
if __name__ == "__main__":
    print("=== Structured Information Extractor ===")
    print("Enter a person's resume or profile text below.")
    print("Type END on a new line when you finish.\n")

    lines = []

    while True:
        line = input()

        if line.strip().upper() == "END":
            break

        lines.append(line)

    input_text = "\n".join(lines).strip()

    if not input_text:
        print("Error: You did not enter any text.")
    else:
        try:
            result = extract_information(input_text)
            print("\nExtracted Information:")
            print(result.model_dump_json(indent=2))
        except Exception as error:
            print(f"\nExtraction failed: {error}")