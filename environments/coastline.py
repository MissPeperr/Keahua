from environments import Environment

class Coastline(Environment):

    def __init__(self, name):
      Environment.__init__(self, name)
    
    def add_animal(self, animal):
        try:
            if animal.aquatic and animal.cell_type == "hypotonic":
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add non-aquatic, or freshwater animals to a river")