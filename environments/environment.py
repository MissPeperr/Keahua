from .contains_animals import ContainsAnimals
from .contains_plants import ContainsPlants
from animals.identifiable import Identifiable


# what do the biomes have in common?
class Environment(ContainsPlants, ContainsAnimals, Identifiable):
    def __init__(self, name):
        Identifiable.__init__(self)
        ContainsAnimals.__init__(self)
        ContainsPlants.__init__(self)
        self.name = name

    def __str__(self):
        return self.name
