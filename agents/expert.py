from llm.huggingface import HuggingFaceLLM


class ExpertAgent:
    def __init__(self):
        self.llm = HuggingFaceLLM()
        self.name = "Expert"

    def think(self, planner_output: str, critic_output: str) -> str:
        prompt = f"""
You are a senior system design expert.

You are given:
1. A proposed solution
2. A critique of that solution

Your job is to:
- Evaluate both
- Correct mistakes
- Provide the most accurate and best-practice solution

Be precise, practical, and technically correct.

Proposed Solution:
{planner_output}

Critique:
{critic_output}

Now provide the final expert-level answer.
"""

        response = self.llm.generate(prompt)

        return response