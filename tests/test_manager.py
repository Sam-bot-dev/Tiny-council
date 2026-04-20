from agents.planner import PlannerAgent
from agents.critic import CriticAgent
from agents.expert import ExpertAgent
from council.manager import CouncilManager


def pretty_print(results):
    print("\n" + "═" * 60)
    print("🏛️  TINY COUNCIL OUTPUT")
    print("═" * 60)

    for agent, response in results.items():  # ✅ FIX HERE
        print("\n" + "─" * 60)
        print(f"🔹 {agent}")
        print("─" * 60)

        print(response.strip())

    print("\n" + "═" * 60 + "\n")


if __name__ == "__main__":
    agents = [
        PlannerAgent(),
        CriticAgent(),
        ExpertAgent()
    ]

    council = CouncilManager(agents)
    user_inp = input("Enter here :-")
    result = council.convene(user_inp)

    pretty_print(result)