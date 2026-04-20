from llm.huggingface import HuggingFaceLLM


class PlannerAgent:
    def __init__(self):
        self.llm = HuggingFaceLLM()
        self.name = "Planner"

    def think(self, query: str) -> str:
        prompt = f"""
You are a senior system design planner.

Your job is to break down problems into clear, structured, step-by-step solutions.
Ensure your answer is COMPLETE and does not stop mid-way.
Guidelines:
- Be practical and actionable
- Use step-by-step format
- Focus on real-world implementation

Problem:
{query}
"""

        response = self.llm.generate(prompt)

        return f"[Planner]\n{response}"