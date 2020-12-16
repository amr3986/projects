
from State2 import State
import heapq
import random
import sys
import time
import math


class StateSpace:

    def __init__(self, n):
        self.startState = State(n)
        self.runTime = {}

    def input(self,lineList):
        self.startState.takeInput(lineList)

    

    def sechdul(self,T):
        coolingRate = 0.0030 #or 0.0030
        
        T=T * 1-coolingRate
        if T <1:
            T = T*0
        return T
        
  
    def Simulated_Annealing(self,heuristic):
        self.startState.setHeuristic(heuristic)
        pq = []
        T = 20   #Temperature initial value
        heapq.heappush(pq, (0, self.startState))
        curNode = heapq.heappop(pq)[1]
        self.initial_state(curNode)
        Global_Max = curNode

        if curNode.isSolvable():
            while T != 0 :
            
                T = self.sechdul(T)   #cooling system
                
                # Diplay the Decreasing of Temperature 
                sys.stdout.write('\rTemperature:  %.2f ' %T)
                sys.stdout.flush()
                time.sleep(0)
                
                #condition to end while loop and return the Globel solution
                if T == 0: return Global_Max
                
                #function to find state Neighbours
                list_Neighbours = curNode.getNeighbourList() 
                #choose random successor of the cuurent node
                Next = random.choice(list_Neighbours) 
                
                Next_Value= Next.heuristicCost
                current_Value = curNode.heuristicCost
                
                #calculate difference Energy between current node and next node 
                ΔE =  current_Value - Next_Value

                # if it is positive Energy mean that Next is good choise 
                if ΔE > 0 :
                    curNode = Next
                # if it is negative Energy mean that Next is bad choise 
                elif math.exp(ΔE/T)> random.random():
                    curNode = Next

                if curNode.heuristicCost < Global_Max.heuristicCost:
                    Global_Max = curNode
        else:
            return "can not be solved"
    
    def initial_state(self, State):
        print("initial state:\n",State)

            
   