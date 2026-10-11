import os


os.environ["GRPC_VERBOSITY"] = "NONE"
os.environ["MIN_LOG_LEVEL"] = "3" #3 means fatal, 2 means error, 1 means warning, 0 means info


from dotenv import load_dotenv
from google import genai

load_dotenv()


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explain python-lists in short and simple")

print(response.text)