from environments import Environment

class Grassland(Environment):

    def __init__(self, name):
      Environment.__init__(self, name)

    def add_animal(self, animal):
        try:
            if animal.terrestrial:
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError(f'The {animal.species} can\'t live in the {self.name} Grassland. {add_color("Must be an animal of terrestrial descent.", "FAIL")}')      