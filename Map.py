class Map:
    def __init__(self, name):
        self.name = name
        self.cities = []
    
    def addCity(self, city):
        self.cities.append(city)
        
    def getCity(self, name):
        for city in self.cities:
            if city.name.upper() == name.upper():
                return city
        return None
    
    def removeCity(self, name):
        for city in self.cities:
            if city.name == name:
                self.cities.remove(city)
                return True
        return False
    
    def getCities(self):
        return self.cities