'''
Docstring for tests.test_manager

when you run the test file run the file in (module mode) rather than in (script mode) 

python -m tests.test_manager (for Windows)

python3 -m tests.test_manager (for mac )
'''

# this is for testing manager , so that it works perfectly...
from agents.planner import PlannerAgent
from agents.critic import CriticAgent
from council.manager import CouncilManager
# print(dir(CouncilManager))

if __name__ == "__main__":
    agents = [
        PlannerAgent(),
        CriticAgent()
    ]

    council = CouncilManager(agents)
    result = council.convene("Design a secure login system")

    for agent, response in result.items():
        print(f"{agent}: {response}")
