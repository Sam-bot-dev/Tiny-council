from agents.planner import PlannerAgent
from agents.critic import CriticAgent
from agents.expert import ExpertAgent
from council.manager import CouncilManager
from cli.banner3 import show_banner
from cli.display import pretty_print

def run():
    agents = [
        PlannerAgent(),
        CriticAgent(),
        ExpertAgent()
    ]

    council = CouncilManager(agents)

    while True:
        query = input("Enter Here\n> ")

        if query.lower() == "exit":
            print("Goodbye 👋")
            break

        print("\nCouncil is thinking...\n")

        result = council.convene(query)

        pretty_print(result)


if __name__ == "__main__":
    show_banner()
    run()