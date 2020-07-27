from environments import Environment
from animals import Animal

class Mountain(Environment):

    def __init__(self, name):
      Environment.__init__(self, name)

    def add_animal(self, animal):
        try:
            if animal.high_elevation:
                if animal.age >= animal.min_age_for_release:
                    self.animals.append(animal)
                else:
                    return False
        except AttributeError:
            print(f'The {animal.species} can\'t live on the {self.name} Mountain. {add_color("Must be a high elevation animal. 🗻", "FAIL")}')