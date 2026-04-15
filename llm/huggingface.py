import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# HF_API_KEY = os.getenv("HF_API_KEY")

class HuggingFaceLLM:
    def __init__(self, model: str):
        self.model = model
        self.api_url = f"https://api-inference.huggingface.co/models/{model}"
        self.headers = {
            "Authorization": f"Bearer {HF_API_KEY}"
        }

    def generate(self, prompt: str, max_tokens: int = 200) -> str:
        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": max_tokens,
                "return_full_text": False
            }
        }

        try:
            response = requests.post(
    self.api_url,
    headers=self.headers,
    json=payload,
    timeout=30
)

            print("STATUS:", response.status_code)
            print("RAW RESPONSE:", response.text[:500])
            data = response.json()

            # Handle common HF response formats
            if isinstance(data, list) and "generated_text" in data[0]:
                return data[0]["generated_text"]

            elif isinstance(data, dict) and "error" in data:
                return f"[HF ERROR] {data['error']}"

            else:
                return f"[UNKNOWN RESPONSE] {data}"

        except Exception as e:
            return f"[REQUEST FAILED] {str(e)}"