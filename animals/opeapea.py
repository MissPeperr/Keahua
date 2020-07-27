from animals import Animal
from animals.attributes import Flying

class OpeApeA(Animal, Flying):

    def __init__(self):
        Animal.__init__(self, "Ope'ape'a", 5)
        Flying.__init__(self)
        self.__prey = { "Crickets", "Carrot tops", "Worms", "Lettuce" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The ope\'ape\'a ate {prey} for a meal')
        else:
            print(f'The ope\'ape\'a rejects the {prey}')

    def __str__(self):
        return f'Ope\'ape\'a [{str(self.id)}]'