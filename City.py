class City:
    def __init__ (self, name):
        self.name = name
        self.adjacentCities = []
        self.distances = []
        
    def addAdjacentCity(self, city,distance=0):
        if distance != 0:
            self.distances.append(distance)
        self.adjacentCities.append(city)
    
    def removeAdjacentCity(self, city):
        self.adjacentCities.remove(city)
        self.distances.remove(self.distances[self.adjacentCities.index(city)])
        
    def getDistance(self, city):
        return self.distances[self.adjacentCities.index(city)]
