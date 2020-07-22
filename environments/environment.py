from .contains_animals import ContainsAnimals
from .contains_plants import ContainsPlants

# what do the biomes have in common?
class Environment(ContainsPlants, ContainsAnimals):
    def __init__(self):
        ContainsAnimals.__init__(self)
        ContainsPlants.__init__(self)