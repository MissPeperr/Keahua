def build_facility_report(arboretum):
    print(f'    Aboretum: {arboretum.name}')
    print(f'    Address: {arboretum.address}')
    print(f'*** Rivers in {arboretum.name} ***')

    for river in arboretum.rivers:
        print(f'    [{str(river.id)[:8]}] River {river}')
        for animal in river.animals:
            print(f'        {animal}')
    
    for mountain in arboretum.mountains:
        print(f'    [{str(mountain.id)[:8]}] Mountain {mountain}')
        for animal in mountain.animals:
            print(f'        {animal}')
    
    for grassland in arboretum.grasslands:
        print(f'    [{str(grassland.id)[:8]}] Grassland {grassland}')
        for animal in grassland.animals:
            print(f'        {animal}')
        
    for swamp in arboretum.swamps:
        print(f'    [{str(swamp.id)[:8]}] Swamp {swamp}')
        for animal in swamp.animals:
            print(f'        {animal}')
    
    for coastline in arboretum.coastlines:
        print(f'    [{str(coastline.id)[:8]}] Coastline {coastline}')
        for animal in coastline.animals:
            print(f'        {animal}')
    input("Press any key to continue...")
