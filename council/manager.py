class CouncilManager:
    def __init__(self, agents):
        self.agents = agents

    def convene(self, query: str):
        planner = None
        critic = None
        expert = None

        # Identify agents
        for agent in self.agents:
            if agent.name == "Planner":
                planner = agent
            elif agent.name == "Critic":
                critic = agent
            elif agent.name == "Expert":
                expert = agent

        results = {}

        # Step 1: Planner
        planner_output = planner.think(query)
        results["Planner"] = planner_output

        # Step 2: Critic (reads planner)
        critic_output = critic.think(planner_output)
        results["Critic"] = critic_output

        # Step 3: Expert (reads both)
        expert_output = expert.think(planner_output, critic_output)
        results["Expert"] = expert_output

        return results