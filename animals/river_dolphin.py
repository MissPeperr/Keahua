from animals import Animal
from animals.attributes import Freshwater
from animals.attributes import Swimming

class RiverDolphin(Animal, Freshwater, Swimming):

    def __init__(self):
        Animal.__init__(self, "River Dolphin", 13.0)
        Freshwater.__init__(self)
        Swimming.__init__(self)
        self.__prey = { "Trout", "Mackarel", "Salmon", "Sardine" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The dolphin ate {prey} for a meal')
        else:
            print(f'The dolphin rejects the {prey}')

    def __str__(self):
        return f'River Dolphin [{str(self.id)[:8]}]'
