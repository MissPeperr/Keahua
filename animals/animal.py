import random
from animals.attributes import Identifiable

class Animal(Identifiable):

    def __init__(self, species, min_age):
        Identifiable.__init__(self)
        self.species = species
        self.age = random.uniform(0.0, 14.0)
        self.min_age_for_release = min_age

    def move(self, propulsion, speed):
        return f"{self.species} moves at {speed} meters/sec by {propulsion}"
