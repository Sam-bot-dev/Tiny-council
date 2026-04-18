from llm.huggingface import HuggingFaceLLM


class CriticAgent:
    def __init__(self):
        self.llm = HuggingFaceLLM()
        self.name = "Critic"

    def think(self, query: str) -> str:
        prompt = f"""
You are a strict system design critic.

Your job is to analyze solutions and find:
- security risks
- design flaws
- scalability issues
- missing considerations

Be critical, analytical, and realistic.

Problem:
{query}

Respond with:
- Key risks
- Weak points
- What could go wrong
"""

        response = self.llm.generate(prompt)

        return f"[Critic]\n{response}"