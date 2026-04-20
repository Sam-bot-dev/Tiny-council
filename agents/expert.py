from llm.huggingface import HuggingFaceLLM


class ExpertAgent:
    def __init__(self):
        self.llm = HuggingFaceLLM()
        self.name = "Expert"

    def think(self, query: str) -> str:
        prompt = f"""
You are a senior system design expert.

Your job is to provide:
- the most accurate
- industry-standard
- best-practice solution

Guidelines:
- Be technically correct
- Cover security, scalability, and performance
- Use clear structured steps
- Do not rely on assumptions
- Ensure your answer is COMPLETE and does not stop mid-way

Problem:
{query}

Provide a complete expert-level solution.
"""

        response = self.llm.generate(prompt, max_tokens=700)

        return f"[Expert]\n{response}"