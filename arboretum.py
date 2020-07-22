class Arboretum:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.__rivers = list()
        self.__grasslands = list()
        self.__mountains = list()
        self.__forests = list()
        self.__swamps = list()
        self.__coastlines = list()

    @property
    def rivers(self):
        return self.__rivers

    def annex_river(self, river):
        self.__rivers.append(river)

    @property
    def grasslands(self):
        return self.__grasslands

    def annex_grassland(self, grassland):
        self.__grasslands.append(grassland)

    @property
    def mountains(self):
        return self.__mountains

    def annex_mountain(self, mountain):
        self.__mountains.append(mountain)

    @property
    def forests(self):
        return self.__forests

    def annex_forest(self, forest):
        self.__forests.append(forest)

    @property
    def swamps(self):
        return self.__swamps

    def annex_swamp(self, swamp):
        self.__swamps.append(swamp)

    @property
    def coastlines(self):
        return self.__coastlines

    def annex_coastline(self, coastline):
        self.__coastlines.append(coastline)
