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

    biome_list = list()
    for index, coastline in enumerate(arboretum.coastlines):
        biome_list.append(coastline)

    for index, forest in enumerate(arboretum.forests):
        biome_list.append(forest)

    for index, grassland in enumerate(arboretum.grasslands):
        biome_list.append(grassland)

    for index, mountain in enumerate(arboretum.mountains):
        biome_list.append(mountains)
    
    for index, river in enumerate(arboretum.rivers):
        biome_list.append(river)

    for index, swamp in enumerate(arboretum.swamps):
        biome_list.append(swamp)

    for index, biome in enumerate(biome_list):
        print(f'{add_color(f"{index + 1}.", "bright_cyan")} {biome.name} {type(biome).__name__} [{str(biome.id)[:8]}]: ({len(biome.animals)} animals)')

    print()
    print()
    print(f'{add_color(f"Release the {animal.species} into which biome?", "WARNING")}')
    choice = input("> ")

    # check if choice selected exists as an index on the biome_list
    if int(choice - 1) < len(biome_list):
        biome_list[int(choice) - 1].add_animal(animal)
        arboretum.rivers[int(choice) - 1].add_animal(animal)
        


