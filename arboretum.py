class Arboretum:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.__rivers = list()
        self.grasslands = list()

    @property
    def rivers(self):
        return self.__rivers
    
    def annex_river(self, river):
        self.__rivers.append(river)
