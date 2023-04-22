import sys
from Map import Map
from init import loadCities
from DepthFirst import DepthFirst
from UCS import UCS
from AStar import AStar

Portugal = Map("Portugal")
loadCities(Portugal)

start = Portugal.getCity("Viseu")
end = Portugal.getCity("Faro")

if len(sys.argv) == 3:
    start = Portugal.getCity(sys.argv[1])
    end = Portugal.getCity(sys.argv[2])

path, path_distance = AStar().getPath(start, end)

for item in path:
    print (item.name)
print("Total Distance: " + str(path_distance) + " km")