import sys
sys.path.append('../')

from environments import Environment
# from animals.


class Swamp(Environment):

    def __init__(self, name):
      Environment.__init__(name)

    def animal_count(self):
        return "This place has a bunch of animals in it"

    # Don't know what to replace IStagnant with yet, since we're not using "Interfaces"
    # def addInhabitant(self, item):
    #     if not isinstance(item, IStagnant):
    #         raise TypeError(f"{item} is not of type IStagnant")
    #     self.inhabitants.append(item)
