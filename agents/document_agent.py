import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

# configure Gemini with your API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

class DocumentAgent:

    def __init__(self):
        # Use a model that your API key supports
        self.model = genai.GenerativeModel("models/gemini-2.5-flash")

    def handle(self, query, text):
        if not text:
            return "No document was uploaded."

        prompt = f"""
You are a helpful assistant. 
Here is the document text:

{text}

User question: {query}

Answer clearly and concisely:
"""

        response = self.model.generate_content(prompt)
        return response.text
