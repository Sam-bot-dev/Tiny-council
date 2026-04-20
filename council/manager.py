from council.consensus import ConsensusEngine


class CouncilManager:
    def __init__(self, agents):
        self.agents = agents
        self.consensus = ConsensusEngine()  # ✅ THIS LINE WAS MISSING

    def convene(self, query: str):
        results = {}

        # Step 1: collect agent outputs
        for agent in self.agents:
            results[agent.name] = agent.think(query)

        # Step 2: run consensus
        final_decision = self.consensus.decide(query, results)

        # Step 3: return structured output
        return {
            "agents": results,
            "consensus": final_decision
        }