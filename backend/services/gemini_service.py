import base64
import json
import os
import re

from google import genai
from google.genai import types
from google.genai.errors import APIError
from models.schemas import SyllabusGradingScale

# can change Gemini's model to the user's peference
GEMINI_MODEL = "gemini-3.8-flash"


# this will be used to clean up the letter grades extracted by Gemini
def clean_grade_letter(letter: str) -> str:
    match = re.search(r'[A-F][+-]?', letter.strip())
    return match.group(0) if match else letter.strip()

# Gemini will scan the given PDF (syllabus) to retrieve the grade scales
def parse_syllabus_pdf(pdf_bytes: bytes):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not set in .env")

    client = genai.Client(api_key=api_key)
    target_model = GEMINI_MODEL

    try:
        pdf_base64 = base64.b64encode(pdf_bytes).decode("utf-8")

        response = client.models.generate_content(
            model=target_model,
            contents=[
                {
                    "inline_data": {
                        "mime_type": "application/pdf",
                        "data": pdf_base64
                    }
                },
                "Extract the complete letter grade scale and percentage thresholds from this syllabus PDF. Return only the grading scale."
            ],
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=SyllabusGradingScale
            )
        )

        # clean response test before parsing
        raw = response.text.strip()
        raw = raw.removeprefix("```json").removeprefix("```").removesuffix("```").strip()

        parsed = json.loads(raw)

        for entry in parsed.get("grading_scale", []):
            entry["letter"] = clean_grade_letter(entry["letter"])

        return parsed
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Failed to parse Gemini response as JSON: {str(e)}")
    except APIError as e:
        raise RuntimeError(f"Gemini API Error ({e.code}): {e.message}")
    except Exception as e:
        raise RuntimeError(f"Unexpected error: {str(e)}")
    
# used if the user/student wants to copy and past text instead of uploading a file
def parse_syllabus_text(text: str):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not set in .env")

    client = genai.Client(api_key=api_key)
    target_model = GEMINI_MODEL

    try:
        chat = client.chats.create(
            model = target_model,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=SyllabusGradingScale
            )
        )
        response = chat.send_message(f"Extract the complete letter grade scale and percentage thresholds from this syllabus text:\n\n{text}")
        parsed = json.loads(response.text)

        # clean up Gemini's output - fix the main problem - LOOK into this more
        for entry in parsed.get("grading_scale", []):
            entry["letter"] = clean_grade_letter(entry["letter"])

        return parsed

    except APIError as e:
        raise RuntimeError(f"Gemini API Error ({e.code}): {e.message}")
    except Exception as e:
        raise RuntimeError(f"Unexpected error: {str(e)}")