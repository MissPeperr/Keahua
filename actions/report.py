def build_facility_report(arboretum):
    print(f'    Aboretum: {arboretum.name}')
    print(f'    Address: {arboretum.address}')

    print(f'*** Coastlines in {arboretum.name} ***')
    for coastline in arboretum.coastlines:
        print(f'    [{str(coastline.id)[:8]}] {coastline} Coastline')
        for animal in coastline.animals:
            print(f'        {animal}')

    print(f'*** Forests in {arboretum.name} ***')
    for forest in arboretum.forests:
        print(f'    [{str(forest.id)[:8]}] {forest} Forest')
        for animal in forest.animals:
            print(f'        {animal}')

    print(f'*** Grasslands in {arboretum.name} ***')
    for grassland in arboretum.grasslands:
        print(f'    [{str(grassland.id)[:8]}] {grassland} Grassland')
        for animal in grassland.animals:
            print(f'        {animal}')

    print(f'*** Mountains in {arboretum.name} ***')
    for mountain in arboretum.mountains:
        print(f'    [{str(mountain.id)[:8]}] {mountain} Mountain')
        for animal in mountain.animals:
            print(f'        {animal}')

    print(f'*** Rivers in {arboretum.name} ***')
    for river in arboretum.rivers:
        print(f'    [{str(river.id)[:8]}] {river} River')
        for animal in river.animals:
            print(f'        {animal}')

    print(f'*** Swamps in {arboretum.name} ***')
    for swamp in arboretum.swamps:
        print(f'    [{str(swamp.id)[:8]}] {swamp} Swamp')
        for animal in swamp.animals:
            print(f'        {animal}')

    input("Press any key to continue...")
