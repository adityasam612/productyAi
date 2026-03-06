import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # reads .env in ai_assistant/

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_ai(prompt: str) -> str:
    # example – adjust to the actual API you use
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content