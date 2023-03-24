class UCS:
    def __init__(self):
        self.path = []
        self.visited = []

    def ucs(self,start,end):
        self.path.append(start)
        self.visited.append(start)
        if start == end:
            return True
        nodes = start.adjacentCities.copy()
        nodes.sort(key=lambda x: start.getDistance(x))
        for node in nodes:
            if node not in self.visited:
                if self.ucs(node, end):
                    return True
        self.path.pop()
        return False
    
    def getPath(self, start, end):
        self.ucs(start, end)
        return self.path
            