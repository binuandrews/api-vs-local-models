import os
import sys

from dotenv import load_dotenv
from huggingface_hub.errors import HfHubHTTPError
from huggingface_hub import InferenceClient
from requests.exceptions import RequestException


def main():
    load_dotenv()

    api_key = os.getenv("HUGGINGFACE_API_KEY")
    if not api_key:
        print("Set HUGGINGFACE_API_KEY or HF_TOKEN in your .env file.", file=sys.stderr)
        return 1

    client = InferenceClient(
        model="meta-llama/Llama-3.1-8B-Instruct",
        provider="auto",
        api_key=api_key,
    )

    prompt = "Write a short poem about the beauty of nature."

    try:
        response = client.chat_completion(
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
        )
    except HfHubHTTPError as error:
        status_code = error.response.status_code if error.response is not None else None
        if status_code == 402:
            message = "Hugging Face inference credits are exhausted. Add credits or use a plan with included credits."
        elif status_code in (401, 403):
            message = "Hugging Face rejected the token. Check its value and permissions."
        else:
            message = f"Hugging Face inference failed (HTTP {status_code or 'unknown'}). Check the model and provider settings."
        print(message, file=sys.stderr)
        return 1
    except RequestException:
        print("Could not connect to Hugging Face. Check your internet connection and try again.", file=sys.stderr)
        return 1

    print(response.choices[0].message.content or "")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())