from environments import Environment
from animals import Animal

class Mountain(Environment):

    def __init__(self, name):
      Environment.__init__(self, name)

    def add_animal(self, animal):
        try:
            if animal.aquatic and animal.cell_type == "hypertonic":
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add non-aquatic, or saltwater animals to a river")