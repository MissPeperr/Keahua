import time
from .cli_colors import CLColors

def loading_sequence():
    for num in range(0, 15):
        print("#", end="", flush=True)
        time.sleep(0.25)
    print(f"  {CLColors.OKGREEN}Done! 👍{CLColors.ENDC}")