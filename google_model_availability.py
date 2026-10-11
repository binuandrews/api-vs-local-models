import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

models = client.models.list()
for model in models:
    if model.supported_actions and "generateContent" in model.supported_actions:
        print(model.name, model.description)
    else:
        print(model.name, getattr(model, "supported_actions", []))