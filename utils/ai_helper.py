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

        client = genai.Client(
            api_key=API_KEY
        )

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return {
            "success": True,
            "message": response.text
        }

    except Exception as e:

        error = str(e)

        if (
            "429" in error
            or "RESOURCE_EXHAUSTED" in error
            or "quota" in error.lower()
        ):

            return {

                "success": False,

                "message": """
## ⚠️ AI Insights Temporarily Unavailable

The Gemini API quota has been exhausted.

The remaining features continue to work normally:

- ✅ Dashboard
- ✅ KPI Cards
- ✅ Data Quality Analysis
- ✅ Interactive Charts
- ✅ Visualizations
- ✅ PDF Export

Please try again later or configure another API key.
"""

            }

        if "503" in error:

            return {

                "success": False,

                "message": """
## ⚠️ AI Service Busy

Gemini is currently experiencing high demand.

Please try again later.
"""

            }

        return {

            "success": False,

            "message": f"Unexpected error:\n\n{error}"

        }