from StateSpace2 import StateSpace
from Constant2 import Constant
import timeit


file = open("input.txt", "r")
isFirstLine = True
state = None
lineList = []
for line in file:
    if isFirstLine:
        state = StateSpace(int(line))
        isFirstLine = False
    else:
        lineList.append(line.strip())
state.input(lineList)

start = timeit.timeit()
solution = state.Simulated_Annealing(Constant.ManhattanHeuristic)
print("\n\nSolution :\n", solution)
end = timeit.timeit()
print("\n Execution time:", str(end - start))










   
