from queue import PriorityQueue
from City import City
from copy import deepcopy


class UCS:
    def __init__(self):
        self.nodes = []
        self.visited = []
        self.path = []

    def ucs(self, start, end, distance=0):
        if start.name == end.name:
            return True

        for node in start.adjacentCities:
            self.nodes.append(
                [start.getDistance(node) + distance, node, start])

        self.nodes.sort(key=lambda x: x[0])

        for dis, node, startNode in self.nodes:
            if node not in self.visited:
                distance = dis
                self.visited.append(node)
                if self.ucs(node, end, distance):
                    return True
        return False

    def getPath(self, start, end):
        self.ucs(start, end)
        self.getPathRecursive(start, end)
        self.path.reverse()
        return self.path, self.calcDistance()
    
    def calcDistance(self):
        distance = 0
        for i in self.path:
            if i == self.path[-1]:
                break
            distance += i.getDistance(self.path[self.path.index(i) + 1])
        return distance

    def getPathRecursive(self, start, end):
        self.path.append(end)
        if start.name == end.name:
            return
        for index, item in enumerate(self.nodes):
            if item[1].name == end.name:
                self.getPathRecursive(start, self.nodes[index][2])
                break
