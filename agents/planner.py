from agents.base_agent import BaseAgent


class PlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Planner",
            role="Breaks down the problem and proposes a plan.",
            system_prompt="You are a planning-focused AI agent."
        )

    def think(self, query: str) -> str:
        return f"[PLAN] High-level plan for: {query}"
