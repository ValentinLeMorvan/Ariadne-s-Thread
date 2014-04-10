from Parsing import Parse
from Start import Start
from datetime import datetime
from PathBasedAlgo import ConnectedComponents
from ReduceMatrix import ReduceMatrix
from LongestPath import BellmanFord
from end import End

fileName = raw_input("Enter the name of the file containing the matrix: ")
AdjacencyList = Parse(fileName)

Levels = ConnectedComponents(AdjacencyList)
Levels.reverse()
for i in range(0, len(Levels)):
    Levels[i].reverse()
    print "Level", i+1 , "contains the places:" , Levels[i]




ReducedMatrix = ReduceMatrix(AdjacencyList, Levels)
print "\nThe map of the links between the levels correspond to the matrix:"
for i in ReducedMatrix:
    print i

start = Start(ReducedMatrix)
end = End(ReducedMatrix)

longestPath = BellmanFord(ReducedMatrix, start, end)
print "\nThe longest path is: ", longestPath


s = raw_input("Appuyez sur ENTREE pour terminer le programme.")
