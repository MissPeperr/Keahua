from animals import Animal
from animals.attributes import Flying
from animals.attributes import Walking
from animals.attributes import Swimming
from animals.attributes import Terrestrial

class NeneGoose(Animal, Flying, Walking, Swimming, Terrestrial):

    def __init__(self):
        Animal.__init__(self, "Nene Goose", 7)
        Flying.__init__(self)
        Walking.__init__(self)
        Swimming.__init__(self)
        Terrestrial.__init__(self)
        self.__prey = { "Crickets", "Worms", "'Ōhelo berry" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The nene goose ate {prey} for a meal')
        else:
            print(f'The nene goose rejects the {prey}')

    def __str__(self):
        return f'Nene Goose [{str(self.id)}]'
