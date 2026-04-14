import pyfiglet
import time
import sys
from termcolor import colored

# 🎯 Typing animation
def type_print(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# 🎯 Gradient effect (manual)
def gradient_text(text):
    colors = ["cyan", "blue", "magenta", "red"]
    result = ""
    for i, line in enumerate(text.split("\n")):
        result += colored(line, colors[i % len(colors)], attrs=["bold"]) + "\n"
    return result

def show_banner():
    # 🧠 Generate banner
    banner = pyfiglet.figlet_format("TINY\nCOUNCIL", font="slant")

    # 🎨 Gradient banner
    print(gradient_text(banner))

    # 🟡 Subtitle (typed)
    type_print(colored("Tiny Council · v0.1", "yellow", attrs=["bold"]), 0.02)
    type_print(colored("Multi-Agent AI Decision System\n", "white"), 0.01)

    print(colored("─" * 50, "grey"))

    # ⚙️ Fake system initialization
    type_print(colored("Initializing system...", "cyan"), 0.02)
    time.sleep(0.3)

    type_print(colored("Loading agents...", "cyan"), 0.02)
    time.sleep(0.3)

    type_print(colored("Consensus Engine: Active", "green"), 0.02)
    time.sleep(0.3)

    print(colored("System Ready 🚀\n", "green", attrs=["bold"]))

    print(colored("─" * 50, "grey"))

    # 📘 Tips section
    type_print(colored("Tips:", "yellow", attrs=["bold"]), 0.01)
    type_print("1. Ask complex questions for better results", 0.005)
    type_print("2. View agent reasoning for deeper insights", 0.005)
    type_print("3. Type 'exit' to quit\n", 0.005)

    print(colored("─" * 50, "grey"))
    choice = input("Want to see architecture [Y/n]: ").lower()

    if choice == "y":
        print("Showing architecture...\n")
        print(r'''           User Query
               |
               v
      +-------------------+
      |  Council Manager  |
      +-------------------+
        |       |       |
        v       v       v
+---------+ +---------+ +---------+
| Planner | | Critic  | | Expert  |
+---------+ +---------+ +---------+
      \         |         /
       \        |        /
        v       v       v
      +-------------------+
      | Consensus Engine  |
      +-------------------+
                |
                v
   Final Answer + Reasoning Trace''')
    else:
        type_print("Ok let's start\n",0.05)
        type_print("Do you want 1 agent standalone with 3 agent_mindset or 3 different llms?",0.05)

show_banner()