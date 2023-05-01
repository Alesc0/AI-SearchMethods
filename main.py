import sys
from Map import Map
from UserInterface import UserInterface
from init import loadCities
from DepthFirst import DepthFirst
from UCS import UCS
from AStar import AStar


Portugal = Map("Portugal")
loadCities(Portugal)


interface = UserInterface(Portugal)
interface.mainloop()