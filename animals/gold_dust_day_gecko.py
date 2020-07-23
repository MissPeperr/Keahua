from animals import Animal
from animals.attributes import Terrestrial
from animals.attributes import Walking


class GoldDustDayGecko(Animal, Terrestrial, Walking):

    def __init__(self):
        Animal.__init__(self, "Gold Dust Day Gecko")
        Terrestrial.__init__(self)
        Walking.__init__(self, 4)
        self.__prey = {"Flies", "Crickets"}

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The gold dust day gecko ate {prey} for a meal')
        else:
            print(f'The gold dust day gecko rejects the {prey}')

    def __str__(self):
        return f'Gold Dust Day Gecko [{str(self.id)}]'
