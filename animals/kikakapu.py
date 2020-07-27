from animals import Animal
from animals.attributes import Freshwater
from animals.attributes import Swimming

class Kikakapu(Animal, Freshwater, Swimming):

    def __init__(self):
        Animal.__init__(self, "Kīkākapu", 1)
        Freshwater.__init__(self)
        Swimming.__init__(self)
        self.__prey = { "Goldfish", "Shrimp", "Sardine" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The kīkākapu ate {prey} for a meal')
        else:
            print(f'The kīkākapu rejects the {prey}')

    def __str__(self):
        return f'Kīkākapu [{str(self.id)}]'
