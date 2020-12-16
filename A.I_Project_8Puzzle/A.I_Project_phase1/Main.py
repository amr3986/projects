from StateSpace import StateSpace
from Constant import Constant


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
state.AstarSearch(Constant.ManhattanHeuristic)

