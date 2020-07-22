from animals import Animal
from animals import Terrestrial
from animals import Walking
from animals import Identifiable


class HawaiianHappyFaceSpider(Animal, Terrestrial, Walking):

    def __init__(self):
        Animal.__init__(self, "Hawaiian Happy-Face Spider")
        Terrestrial.__init__(self)
        Walking.__init__(self)
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
        return f'Hawaiian Happy-Face Spider [{str(self.id)}]'
