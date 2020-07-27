import os
from arboretum import Arboretum
from actions.menu_header import print_header
from actions.annex import annex_habitat
from actions.release_animal import release_animal
from actions.report import build_facility_report
from actions.utilities import clear
from actions.utilities import add_color

keahua = Arboretum("Keahua Arboretum", "123 Paukauila Lane")


def build_menu():
    clear()
    print_header()
    print()
    print(f'{add_color("1.", "bright_cyan")} Annex Habitat')
    print(f'{add_color("2.", "bright_cyan")} Release Animal into Habitat')
    print(f'{add_color("3.", "bright_cyan")} Feed Animal')
    print(f'{add_color("4.", "bright_cyan")} Add Plant to Habitat')
    print(f'{add_color("5.", "bright_cyan")} Display Facility Report')
    print(f'{add_color("6.", "bright_cyan")} Exit')
    print()


def main_menu():
    """Show Keahua Action Options

    Arguments: None
    """
    build_menu()

    print(f'{add_color("What would you like to do?", "WARNING")}')
    choice = input('> ')

    if choice == "1":
        annex_habitat(keahua)

    if choice == "2":
        clear()
        release_animal(keahua, False)

    if choice == "3":
        pass

    if choice == "4":
        pass

    if choice == "5":
        build_facility_report(keahua)

    if choice != "6":
        main_menu()


main_menu()
