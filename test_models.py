import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

print("\nAvailable Models:\n")
for m in genai.list_models():
    print(m.name)
