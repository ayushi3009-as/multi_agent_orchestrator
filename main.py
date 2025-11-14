import os
from dotenv import load_dotenv
from openai import OpenAI

# Load the .env file
load_dotenv()

# Get your key from the environment (automatically)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Test it
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello from VS Code!"}]
)

print(response.choices[0].message.content)
