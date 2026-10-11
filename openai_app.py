import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY") or os.getenv("OPEN_AI_API_KEY"))

prompt = "What is the capital of France? Give me the answe in a paragraph"

response = client.chat.completions.create(
    model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}], max_tokens=500)

print(response.choices[0].message.content.strip())

