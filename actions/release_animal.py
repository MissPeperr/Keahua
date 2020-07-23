import os
import time
from animals import RiverDolphin
from animals import GoldDustDayGecko
from animals import HawaiianHappyFaceSpider
from animals import Kikakapu
from animals import NeneGoose
from animals import OpeApeA
from animals import Pueo
from animals import Ulae
from actions.menu_header import print_header
from actions.loading import loading_sequence
from actions.cli_colors import CLColors
from actions.utilities import clear
from actions.utilities import add_color

def release_animal(arboretum, wrong_choice):
    """
        Prompts user to create an Animal to release into an Enviornment.
    """

    animal = None

    if wrong_choice != True:
        print_header()

    print()
    print(f'{add_color("1.", "bright_cyan")} Gold Dust Day Gecko')
    print(f'{add_color("2.", "bright_cyan")} Hawaiian Happy-Face Spider')
    print(f'{add_color("3.", "bright_cyan")} Kīkākapu')
    print(f'{add_color("4.", "bright_cyan")} Nene Goose')
    print(f'{add_color("5.", "bright_cyan")} Ope\'ape\'a')
    print(f'{add_color("6.", "bright_cyan")} Pueo')
    print(f'{add_color("7.", "bright_cyan")} River Dolphin')
    print(f'{add_color("8.", "bright_cyan")} \'Ulae')
    print()
    
    print(f'{add_color("Select an animal to release", "WARNING")}{CLColors.ENDC}')
    choice = input("> ")

    if choice == "1":
        animal = GoldDustDayGecko()

    elif choice == "2":
        animal = HawaiianHappyFaceSpider()

    elif choice == "3":
        animal = Kikakapu()
    
    elif choice == "4":
        animal = NeneGoose()
    
    elif choice == "5":
        animal = OpeApeA()

    elif choice == "6":
        animal = Pueo()
    
    elif choice == "7":
        animal = RiverDolphin()

    elif choice == "8":
        animal = RiverDolphin()

    else:
        wrong_choice = True
        clear()
        print(f'{add_color(f"{choice} is not an animal. Please make another selection.", "FAIL")}')
        print()
        release_animal(arboretum, wrong_choice)

    print(f'Getting the {animal.species} ready...')
    loading_sequence()
    time.sleep(1.5)
    clear()

    print(f'{add_color("Available Biomes:", "HEADER")}')
    print()
    for index, coastline in enumerate(arboretum.coastlines):
        print(f'{add_color(f"{index + 1}.", "bright_cyan")} {coastline} Coastline [{str(coastline.id)[:8]}]: ({len(coastline.animals)} animals)')

    for index, forest in enumerate(arboretum.forests):
        print(f'{add_color(f"{index + 1}.", "bright_cyan")} {forest} Forest [{str(forest.id)[:8]}]: ({len(forest.animals)} animals)')

    for index, grassland in enumerate(arboretum.grasslands):
        print(f'{add_color(f"{index + 1}.", "bright_cyan")} {grassland} Grassland [{str(grassland.id)[:8]}]: ({len(grassland.animals)} animals)')

    for index, mountain in enumerate(arboretum.mountains):
        print(f'{add_color(f"{index + 1}.", "bright_cyan")} {mountain} Mountain [{str(mountain.id)[:8]}]: ({len(mountain.animals)} animals)')
    
    for index, river in enumerate(arboretum.rivers):
        print(f'{add_color(f"{index + 1}.", "bright_cyan")} {river} River [{str(river.id)[:8]}]: ({len(river.animals)} animals)')

    for index, swamp in enumerate(arboretum.swamps):
        print(f'{add_color(f"{index + 1}.", "bright_cyan")} {swamp} Swamp [{str(swamp.id)[:8]}]: ({len(swamp.animals)} animals)')

    print()
    print()
    print(f'{add_color(f"Release the {animal.species} into which biome?", "WARNING")}')
    choice = input("> ")

    arboretum.rivers[int(choice) - 1].add_animal(animal)


