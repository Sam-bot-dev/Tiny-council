import pyfiglet # looks not good but has good things 
from termcolor import colored

def show_banner():
    text = "TINY\nCOUNCIL"

    # Generate block font
    banner = pyfiglet.figlet_format(text, font="block")

    # Split lines
    lines = banner.split("\n")

    # Shadow effect (print slightly offset)
    for line in lines:
        print(colored(" " + line, "red"))  # shadow layer

    # Main text
    for line in lines:
        print(colored(line, "yellow", attrs=["bold"]))

    # Subtitle
    print()
    print(colored("Welcome to Tiny Council", "yellow", attrs=["bold"]))
    print(colored("Multi-Agent AI Decision System\n", "white"))

    # Info box (Claude style)
    print(colored("Security notes:", "yellow", attrs=["bold"]))
    print(colored("1. AI agents may disagree", "white"))
    print(colored("2. Always review final decisions", "white"))
    print(colored("3. System prioritizes safe reasoning\n", "white"))

    print(colored("Press Enter to continue...", "cyan"))
show_banner()