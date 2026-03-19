import pyfiglet
from termcolor import colored

def show_banner():
    # Use a better font (try: 'slant', 'big', 'block', 'banner3-D')
    banner = pyfiglet.figlet_format("TINY COUNCIL", font="slant")

    # Gradient-like effect (manual color layering)
    lines = banner.split("\n")
    colors = ["cyan", "blue", "magenta", "red"]

    colored_banner = ""
    for i, line in enumerate(lines):
        color = colors[i % len(colors)]
        colored_banner += colored(line, color, attrs=["bold"]) + "\n"

    print(colored_banner)

    # Subtitle
    print(colored("Multi-Agent AI Decision System\n", "white", attrs=["bold"]))

    # Divider
    print(colored("─" * 50, "grey"))

    # Tips (Gemini-style)
    print(colored("Tips:", "yellow", attrs=["bold"]))
    print(colored("1. Ask complex questions", "white"))
    print(colored("2. System shows agent reasoning", "white"))
    print(colored("3. Type 'exit' to quit\n", "white"))

    print(colored("─" * 50, "grey"))
show_banner()