from animals import Animal
from animals.attributes import Flying
from animals.attributes import Walking

class Pueo(Animal, Flying, Walking):

    def __init__(self):
        Animal.__init__(self, "Pueo")
        Flying.__init__(self)
        Walking.__init__(self)
        self.__prey = { "Mongoose", "Rats", "Field Mice" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The pueo ate {prey} for a meal')
        else:
            print(f'The pueo rejects the {prey}')

    def __str__(self):
        return f'Pueo [{str(self.id)}]'
