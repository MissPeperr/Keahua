from actions.utilities import add_color

def build_facility_report(arboretum):
    print(f'    Aboretum: {arboretum.name}')
    print(f'    Address: {arboretum.address}')

    if len(arboretum.coastlines) > 0:
        print(f'*** {add_color(f"Coastlines in {arboretum.name}", "bright_cyan")} ***')
        for coastline in arboretum.coastlines:
            print(f'    [{str(coastline.id)[:8]}] {coastline} Coastline')
            for animal in coastline.animals:
                print(f'        {animal}{str(animal.id)[:8]}')

    if len(arboretum.forests) > 0:
        print(f'*** {add_color(f"Forests in {arboretum.name}", "bright_cyan")} ***')
        for forest in arboretum.forests:
            print(f'    [{str(forest.id)[:8]}] {forest} Forest')
            for animal in forest.animals:
                print(f'        {animal}{str(animal.id)[:8]}')

    if len(arboretum.grasslands) > 0:
        print(f'*** {add_color(f"Grasslands in {arboretum.name}", "bright_cyan")} ***')
        for grassland in arboretum.grasslands:
            print(f'    [{str(grassland.id)[:8]}] {grassland} Grassland')
            for animal in grassland.animals:
                print(f'        {animal}{str(animal.id)[:8]}')

    if len(arboretum.mountains) > 0:
        print(f'*** {add_color(f"Mountains in {arboretum.name}", "bright_cyan")} ***')
        for mountain in arboretum.mountains:
            print(f'    [{str(mountain.id)[:8]}] {mountain} Mountain')
            for animal in mountain.animals:
                print(f'        {animal}{str(animal.id)[:8]}')

    if len(arboretum.rivers) > 0:
        print(f'*** {add_color(f"Rivers in {arboretum.name}", "bright_cyan")} ***')
        for river in arboretum.rivers:
            print(f'    [{str(river.id)[:8]}] {river} River')
            for animal in river.animals:
                print(f'        {animal}{str(animal.id)[:8]}')

    if len(arboretum.swamps) > 0:
        print(f'*** {add_color(f"Swamps in {arboretum.name}", "bright_cyan")} ***')
        for swamp in arboretum.swamps:
            print(f'    [{str(swamp.id)[:8]}] {swamp} Swamp')
            for animal in swamp.animals:
                print(f'        {animal}{str(animal.id)[:8]}')

    input("Press any key to go back to the main menu.")
