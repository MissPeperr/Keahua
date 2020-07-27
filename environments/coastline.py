from environments import Environment

class Coastline(Environment):

    def __init__(self, name):
      Environment.__init__(self, name)
    
    def add_animal(self, animal):
        try:
            if animal.aquatic and animal.cell_type == "hypotonic":
                if animal.age >= animal.min_age_for_release:
                    self.animals.append(animal)
                else:
                    return False
        except AttributeError:
            print(f'The {animal.species} can\'t live in the {self.name} Coastline. {add_color("Cannot add non-aquatic, or freshwater animals to a Coastline.", "FAIL")}')