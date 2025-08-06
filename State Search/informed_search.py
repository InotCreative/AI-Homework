from game_machenics import GameMachanics
from collections import deque
import heapq
from typing import List, Tuple, Optional, Dict, Set, Deque
from functools import cache

class InformedSearch:
    def __init__(self, startState: List[List[int]], goalState: List[List[int]], n: int) -> None:
        self.startState: List[List[int]]    = startState
        self.goalState: List[List[int]]     = goalState
        self.n                              = n
        self.GameMachanics: GameMachanics   = GameMachanics(self.n)
        self.startStateKey: Tuple[int, ...] = self.GameMachanics.flattenState(self.startState)
        self.goalStateKey: Tuple[int, ...]  = self.GameMachanics.flattenState(self.goalState)

    def manhattanCostToGoalHurestic(self, currentState: List[List[int]]) -> int:
        currentValueAndIndices: List[Tuple[int, Tuple[int, int]]] = []
        goalValueAndIndices: List[Tuple[int, Tuple[int, int]]] = []
        totalManhattanDistance: int = 0

        for x in range(0, self.n):
            for y in range(0, self.n):
                currentValueAndIndices.append((currentState[x][y], (x + 1, y + 1)))
                goalValueAndIndices.append((self.goalState[x][y], (x + 1, y + 1)))
        
        for i in range(0, len(currentValueAndIndices)):
            currentValue: Tuple[int, Tuple[int, int]] = currentValueAndIndices[i]

            for j in range(0, len(goalValueAndIndices)):
                currentGoalValue: Tuple[int, Tuple[int, int]] = goalValueAndIndices[j]

                if (currentValue[0] == currentGoalValue[0]):
                    totalManhattanDistance += abs((currentValue[1][0] - currentGoalValue[1][0])) + abs((currentValue[1][1] - currentGoalValue[1][1]))

        return totalManhattanDistance
    
    def greedySearch(self):
        minHeapOfStates: List[Tuple[int, List[List[int]]]] = []
        heapq.heappush(minHeapOfStates, (self.manhattanCostToGoalHurestic(self.startState), self.startState))

        visited: Set[Tuple[int, ...]] = set()
        visited.add(self.startStateKey)

        parents: Dict[Tuple[int, ...], Optional[Tuple[int, ...]]] = {self.startStateKey: None}
        stateMap: Dict[Tuple[int, ...], List[List[int]]] = {self.startStateKey: self.startState}
        
        while minHeapOfStates:
            popedState: Tuple[int, List[List[int]]] = heapq.heappop(minHeapOfStates)
            popedStateKey: Tuple[int, ...] = self.GameMachanics.flattenState(popedState[1])

            if (popedStateKey == self.goalState): break

            for sucessorStates in self.GameMachanics.generateSuccessorStates(popedState[1]):
                sucessorStatesKey: Tuple[int, ...] = self.GameMachanics.flattenState(sucessorStates)

                if sucessorStatesKey not in visited:
                    visited.add(sucessorStatesKey)
                    heapq.heappush(minHeapOfStates, (self.manhattanCostToGoalHurestic(sucessorStates), sucessorStates))
                    parents[sucessorStatesKey] = popedStateKey
                    stateMap[sucessorStatesKey] = sucessorStates
        
        if (self.goalStateKey not in visited): return []

        path: List[List[List[int]]] = []
        current: Tuple[int, ...] = self.goalStateKey

        while current:
            path.append(stateMap[current])
            current = parents[current]
        
        path.reverse()

        return path
    
    def aStarSearch(self):
        minHeapOfStates: List[Tuple[int, List[List[int]]]] = []
        heapq.heappush(minHeapOfStates, (self.manhattanCostToGoalHurestic(self.startState), self.startState))

        visited: Set[Tuple[int, ...]] = set()
        visited.add(self.startStateKey)

        parents: Dict[Tuple[int, ...], Optional[Tuple[int, ...]]] = {self.startStateKey: None}
        stateMap: Dict[Tuple[int, ...], List[List[int]]] = {self.startStateKey: self.startState}
        
        while minHeapOfStates:
            popedState: Tuple[int, List[List[int]]] = heapq.heappop(minHeapOfStates)
            popedStateKey: Tuple[int, ...] = self.GameMachanics.flattenState(popedState[1])

            if (popedStateKey == self.goalState): break

            for sucessorStates in self.GameMachanics.generateSuccessorStates(popedState[1]):
                sucessorStatesKey: Tuple[int, ...] = self.GameMachanics.flattenState(sucessorStates)
                costOfMovingToState = self.GameMachanics.generateCost(sucessorStates, popedState[1])

                if sucessorStatesKey not in visited:
                    visited.add(sucessorStatesKey)
                    heapq.heappush(minHeapOfStates, (self.manhattanCostToGoalHurestic(sucessorStates) + costOfMovingToState + popedState[0], sucessorStates))
                    parents[sucessorStatesKey] = popedStateKey
                    stateMap[sucessorStatesKey] = sucessorStates
        
        if (self.goalStateKey not in visited): return []

        path: List[List[List[int]]] = []
        current: Tuple[int, ...] = self.goalStateKey

        while current:
            path.append(stateMap[current])
            current = parents[current]
        
        path.reverse()

        return path