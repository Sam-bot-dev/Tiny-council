from agents.base_agent import BaseAgent


class CriticAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Critic",
            role="Finds flaws, risks, and edge cases.",
            system_prompt="You are a critical and skeptical AI agent."
        )

    def think(self, query: str) -> str:
        return f"[CRITIQUE] Potential risks in: {query}"
