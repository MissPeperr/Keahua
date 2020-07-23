import os
import time
from environments import Coastline
from environments import Forest
from environments import Grassland
from environments import Mountain
from environments import River
from environments import Swamp
from actions.menu_header import print_header
from actions.utilities import clear
from actions.utilities import add_color
from actions.loading import loading_sequence

def annex_habitat(arboretum):
    clear()
    print_header()
    print()
    print(f'{add_color("1.", "bright_cyan")} Coastline')
    print(f'{add_color("2.", "bright_cyan")} Forest')
    print(f'{add_color("3.", "bright_cyan")} Grassland')
    print(f'{add_color("4.", "bright_cyan")} Mountain')
    print(f'{add_color("5.", "bright_cyan")} River')
    print(f'{add_color("6.", "bright_cyan")} Swamp')

    print()
    print(f'{add_color("Select a habitat", "WARNING")}')
    choice = input("> ")
    biome = None

    if choice == "1":
        clear()
        print(f'{add_color("What is the name for this coastline?", "WARNING")}')
        name = input("> ")
        biome = Coastline(name)
        arboretum.coastlines.append(biome)

    if choice == "2":
        clear()
        print(f'{add_color("What is the name for this forest?", "WARNING")}')
        name = input("> ")
        biome = Forest(name)
        arboretum.forests.append(biome)

    if choice == "3":
        clear()
        print(f'{add_color("What is the name for this grassland?", "WARNING")}')
        name = input("> ")
        biome = Grassland(name)
        arboretum.grasslands.append(biome)

    if choice == "4":
        clear()
        print(f'{add_color("What is the name for this mountain?", "WARNING")}')
        name = input("> ")
        biome = Mountain(name)
        arboretum.mountains.append(biome)

    if choice == "5":
        clear()
        print(f'{add_color("What is the name for this river?", "WARNING")}')
        name = input("> ")
        biome = River(name)
        arboretum.rivers.append(biome)

    if choice == "6":
        clear()
        print(f'{add_color("What is the name for this swamp?", "WARNING")}')
        name = input("> ")
        biome = Swamp(name)
        arboretum.swamps.append(biome)
    
    print(f'Purchasing the {biome.name} {type(biome).__name__}...')
    loading_sequence()
    print(f'Terraforming a bit...')
    loading_sequence()
    time.sleep(1.5)
    clear()
