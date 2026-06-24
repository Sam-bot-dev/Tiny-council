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

    def generate(self, prompt: str, max_tokens: int = 800) -> str:
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
        
'''
Result
==================================================
Tiny Council Benchmark Results
==================================================
Prompts Tested     : 10
Average Latency    : 36.45s
P95 Latency        : 55.00s
Throughput         : 0.03 req/s
Avg Response Size  : 12161 chars
==================================================
'''