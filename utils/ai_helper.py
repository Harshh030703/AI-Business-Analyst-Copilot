import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = None

# Streamlit Cloud
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
except Exception:
    pass

# Local .env
if not API_KEY:
    API_KEY = os.getenv("GOOGLE_API_KEY")


def ask_ai(prompt: str):

    if not API_KEY:
        return {
            "success": False,
            "message": "⚠️ Google API Key not found."
        }

    try:

        client = genai.Client(api_key=API_KEY)

        response = client.models.generate_content(
            model="gemini-3.5-flash",   # <-- Updated model
            contents=prompt
        )

        return {
            "success": True,
            "message": response.text
        }

    except Exception as e:

        error = str(e)

        print(error)

        if "RESOURCE_EXHAUSTED" in error or "429" in error:
            return {
                "success": False,
                "message": "⚠️ Gemini quota exceeded. Please try again later."
            }

        elif "INVALID_ARGUMENT" in error:
            return {
                "success": False,
                "message": "⚠️ Invalid Gemini request."
            }

        elif "API_KEY_INVALID" in error:
            return {
                "success": False,
                "message": "⚠️ Invalid Google API Key."
            }

        elif "503" in error:
            return {
                "success": False,
                "message": "⚠️ Gemini service is temporarily unavailable."
            }

        return {
            "success": False,
            "message": error
        }