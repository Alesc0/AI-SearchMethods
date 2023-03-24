class City:
    def __init__ (self, name):
        self.name = name
        self.adjacentCities = []
        
    def addAdjacentCity(self, city):
        self.adjacentCities.append(city)
    
    def removeAdjacentCity(self, city):
        self.adjacentCities.remove(city)
    