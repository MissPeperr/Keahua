from environments import Environment
from actions.utilities import add_color

class Grassland(Environment):

    def __init__(self, name):
      Environment.__init__(self, name)

    def add_animal(self, animal):
        try:
            if animal.terrestrial and animal.ground_nester:
                if animal.age >= animal.min_age_for_release:
                    self.animals.append(animal)
                else:
                    return False
        except AttributeError:
            print(f'The {animal.species} can\'t live in the {self.name} Grassland. {add_color("Must be an animal of terrestrial descent and nests on the ground. 🌾", "FAIL")}')   