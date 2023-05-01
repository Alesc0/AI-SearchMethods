import haversine as hs

class GreedySearch:
    def __init__(self):
        self.open = []
        self.closed = []
        self.h_costs = {} # heuristic costs
        self.parents = {}
        self.path_distance = 0

    def eager_search(self, start, end):
        self.open.append(start)
        # calculuar a distancia em linha reta entre o no atual e o no final
        self.h_costs[start] = hs.haversine(start.location, end.location, unit=hs.Unit.KILOMETERS)

        while True:
            # no path
            if len(self.open) == 0:
                return False

            # escolher o no com menor custo
            current = min(self.open, key=lambda city: self.h_costs[city])

            # found path
            if current == end:
                print("Reached", end.name + ".")
                break

            self.open.remove(current)
            self.closed.append(current)
            
            for neighbor in current.adjacentCities:
                if neighbor in self.closed:
                    continue

                cost_to_neighbour = self.h_costs[current] + current.getDistance(neighbor)
                cost_neighbour_to_goal = hs.haversine(neighbor.location, end.location, unit=hs.Unit.KILOMETERS)
                total_cost = cost_to_neighbour + cost_neighbour_to_goal

                if neighbor not in self.open or total_cost < self.h_costs[neighbor]:
                    self.parents[neighbor] = current
                    self.h_costs[neighbor] = total_cost
                    if neighbor not in self.open:
                        self.open.append(neighbor)
        
        parent = self.parents[end]
        path = [end]
        
        while parent:
            path.append(parent)
            
            if self.parents.get(parent):
                parent = self.parents[parent]
            else:
                parent = False

        path.reverse()
        for i in range(len(path)-1):
            self.path_distance += path[i].getDistance(path[i+1])
        return path, self.path_distance
    
    def getPath(self, start, end):
        return self.eager_search(start, end)
    