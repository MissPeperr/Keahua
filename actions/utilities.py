import os
from .cli_colors import CLColors

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_color(string, color):
    """
        Adds a specified color to a string.

        Color must be the property of the CLColors class. 
    """
    return f'{getattr(CLColors, color)}{string}{CLColors.ENDC}'