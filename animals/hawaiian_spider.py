from animals import Animal
from animals.attributes import Terrestrial
from animals.attributes import Walking


class HawaiianHappyFaceSpider(Animal, Terrestrial, Walking):

    def __init__(self):
        Animal.__init__(self, "Hawaiian Happy-Face Spider", 0.5)
        Terrestrial.__init__(self)
        Walking.__init__(self, 8)
        self.__prey = {"Crickets", "Flies"}

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The hawaiian happy-face spider ate {prey} for a meal')
        else:
            print(f'The hawaiian happy-face spider rejects the {prey}')

    def __str__(self):
        return f'Hawaiian Happy-Face Spider [{str(self.id)[:8]}]'
