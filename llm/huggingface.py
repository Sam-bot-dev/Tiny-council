from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")


class HuggingFaceLLM:
    def __init__(self, model: str = "mistralai/Mistral-7B-Instruct-v0.2"):
        self.model = model
        self.client = InferenceClient(
            model=model,
            token=HF_API_KEY
        )

    def generate(self, prompt: str, max_tokens: int = 200) -> str:
        try:
            response = self.client.chat_completion(
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                max_tokens=max_tokens
            )

            # 🔥 FIX IS HERE (object access, not dict)
            return response.choices[0].message.content

        except Exception as e:
            print("DEBUG ERROR:", e)
            return f"[HF ERROR] {str(e)}"