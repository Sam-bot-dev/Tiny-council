# Consensus Engine (Conceptual Design) 
'''
Docstring for council.consensus
this is a general agreement (as of opinion or fact) among a group of people or things
here we are going to use it as intelligence layer.

this layer should be able to

1. What should we decide?

2. Why this decision over the others?

explain why it took the decision 

'''

from agents.critic import CriticAgent
from agents.planner import PlannerAgent
from council.manager import CouncilManager


if __name__ == "__main__" :
    agents = [
        PlannerAgent(),
        CriticAgent(),
        PlannerAgent()
    ]
    council = CouncilManager(agents)
    result = council.convene("Design a secure login system")
    ai_responces = {}   # create it BEFORE the loop

    for agent, responce in result.items():
        ai_responces[agent] = responce



         
print(ai_responces)