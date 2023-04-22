import haversine as hs

class AStar:
    def __init__(self):
        self.open = []
        self.closed = []
        self.f_costs = {}
        self.g_costs = {}
        self.parents = {}
        self.path_distance = 0

    def a_star(self,start,end):
        self.open.append(start)
        self.g_costs[start] = 0

        while True:
            if len(self.open) == 0:
                return False

            current = self.open.pop(0)
            self.closed.append(current)

            if current == end:
                print("Reached", end.name + ".")
                break
            

            for neighbor in current.adjacentCities:
                if neighbor in self.closed:
                    continue

                g = self.g_costs[current] + current.getDistance(neighbor)
                h = hs.haversine(neighbor.location, end.location, unit=hs.Unit.KILOMETERS)
                f = g + h

                if neighbor not in self.open or f < self.f_costs[neighbor]:
                    self.parents[neighbor] = current
                    self.f_costs[neighbor] = f
                    self.g_costs[neighbor] = g
                    if neighbor not in self.open:
                        self.open.append(neighbor)
                
        
        parent = self.parents[end]
        path = [end]
        path_distance = self.g_costs[end]
        
        while parent:
            path.append(parent)
            
            if self.parents.get(parent):
                parent = self.parents[parent]
            else:
                parent = False

        path.reverse()
        
        return path, path_distance
    
    def getPath(self, start, end):
        return self.a_star(start, end)