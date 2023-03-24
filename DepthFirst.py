class DepthFirst:
    def __init__(self):
        self.path = []
        self.visited = []

    def dfs(self, start, end):
        self.visited.append(start)
        self.path.append(start)
        if start == end:
            return True
        for node in start.adjacentCities:
            if node not in self.visited:
                if self.dfs(node, end):
                    return True
        self.path.pop()
        return False

    def getPath(self, start, end):
        self.dfs(start, end)
        return self.path
