from environments import Environment
from actions.utilities import add_color


class Forest(Environment):

    def __init__(self, name):
        Environment.__init__(self, name)

    def add_animal(self, animal):
        try:
            if animal.terrestrial and animal.tree_dwelling:
                self.animals.append(animal)
        except AttributeError:
            print(f'The {animal.species} can\'t live in the {self.name} Forest. {add_color("Must be an animal of terrestrial descent and dwells within the trees. 🌳", "FAIL")}')
