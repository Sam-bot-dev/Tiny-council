from typing import List, Dict
from agents.base_agent import BaseAgent

class CouncilManager:
    
    def __init__(self,agents:List[BaseAgent]):
        """
        Orchestrates the flow of a council discussion.
        """
        self.agents = agents
        
    def convene(self,query:str) -> Dict[str,str]:
        """
        Sends the query to all agents and collects their responses.
        """
        responses = {} # empty

        for agent in self.agents:
            try:
                response = agent.think(query)
                responses[agent.name] = response
            except Exception as e:
                responses[agent.name] = f"ERROR: {str(e)}"

        return responses
