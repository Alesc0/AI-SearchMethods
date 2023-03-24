import sys
from Map import Map
from init import loadCities
from DepthFirst import DepthFirst

Portugal = Map("Portugal")
loadCities(Portugal)

start = Portugal.getCity(sys.argv[1])
end = Portugal.getCity(sys.argv[2])

dfs = DepthFirst().getPath(start, end)

for item in dfs:
    print (item.name)