import os
from environments import Coastline
from environments import Forest
from environments import Grassland
from environments import Mountain
from environments import River
from environments import Swamp

def annex_habitat(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Coastline")
    print("2. Forest")
    print("3. Grassland")
    print("4. Mountain")
    print("5. River")
    print("6. Swamp")

    choice = input("Choose your habitat > ")

    if choice == "1":
        name = input("What's the name for this coastline? > ")
        coastline = Coastline(name)
        arboretum.coastlines.append(coastline)

    if choice == "2":
        name = input("What's the name for this forest? > ")
        forest = Forest(name)
        arboretum.forests.append(forest)

    if choice == "3":
        name = input("What's the name for this grassland? > ")
        grassland = Grassland(name)
        arboretum.grasslands.append(grassland)

    if choice == "4":
        name = input("What's the name for this mountain? > ")
        mountain = Mountain(name)
        arboretum.mountains.append(mountain)

    if choice == "5":
        name = input("What's the name for this river? > ")
        river = River(name)
        arboretum.rivers.append(river)

    if choice == "6":
        name = input("What's the name for this swamp? > ")
        swamp = Swamp(name)
        arboretum.swamps.append(swamp)
