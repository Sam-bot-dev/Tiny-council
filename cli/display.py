def pretty_print(data):
    results = data["agents"]
    consensus = data["consensus"]

    print("\n" + "═" * 60)
    print("🏛️  TINY COUNCIL OUTPUT")
    print("═" * 60)

    for agent, response in results.items():
        print("\n" + "─" * 60)
        print(f"🔹 {agent}")
        print("─" * 60)
        print(response.strip())

    print("\n" + "═" * 60)
    print("🏆 FINAL DECISION")
    print("═" * 60)

    print(f"\nBest Agent: {consensus['best_agent']}")
    print("\nFinal Answer:\n")
    print(consensus["final_answer"])

    print("\n📊 Scores:")
    for agent, score in consensus["scores"].items():
        print(f"- {agent}: {score}")

    print("\n🧠 Reason:")
    print(consensus["reason"])

    print("\n" + "═" * 60 + "\n")