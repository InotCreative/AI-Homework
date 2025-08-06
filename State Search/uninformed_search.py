from game_machenics import GameMachanics
from collections import deque
import heapq
from typing import List, Tuple, Optional, Dict, Set, Deque
from functools import cache

class UninformedSearch:
    def __init__(self, startState: List[List[int]], goalState: List[List[int]], n: int) -> None:
        self.startState: List[List[int]]    = startState
        self.goalState: List[List[int]]     = goalState
        self.n                              = n
        self.GameMachanics: GameMachanics   = GameMachanics(self.n)
        self.startStateKey: Tuple[int, ...] = self.GameMachanics.flattenState(self.startState)
        self.goalStateKey: Tuple[int, ...]  = self.GameMachanics.flattenState(self.goalState)
    
    @cache
    def bredthFirstSearch(self) -> List[List[List[int]]]:
        queueOfStates: Deque[List[List[int]]] = deque()  # Holds all states to explore
        queueOfStates.append(self.startState)
        
        visited: Set[Tuple[int, ...]] = set()            # Set to keep track of visited states so we don't expore states we already explored
        visited.add(self.startStateKey)                                                          # Add the first state to visited
        
        parents: Dict[Tuple[int, ...], Optional[Tuple[int, ...]]] = {self.startStateKey: None}   # The start state has no parents as its the first state
        stateMap: Dict[Tuple[int, ...], List[List[int]]] = {self.startStateKey: self.startState} # Keeps the map between the hashed version of the state and the actual state

        while queueOfStates:
            poppedState: List[List[int]] = queueOfStates.popleft()
            poppedStateKey: Tuple[int, ...] = self.GameMachanics.flattenState(poppedState)

            if poppedStateKey == self.goalStateKey: break

            for successorStates in self.GameMachanics.generateSuccessorStates(poppedState):            # Generate all sucessor states
                successorStatesKey: Tuple[int, ...] = self.GameMachanics.flattenState(successorStates) # Hash the sucessor states to make set operations quicker

                if successorStatesKey not in visited:
                    visited.add(successorStatesKey)
                    parents[successorStatesKey] = poppedStateKey      # Parents are stored as key value pair where the key is all the successor states that can be generated from a parent
                    stateMap[successorStatesKey] = successorStates    # Mappings are hash values of the state to the actual state
                    queueOfStates.append(successorStates)
        
        if self.goalStateKey not in parents: return []                # If the goal key doesnt exist in the dictionary than the key doesn't exist

        path: List[List[List[int]]] = []
        currentKey: Optional[Tuple[int, ...]] = self.goalStateKey
        # Start at the goal state because if we start at the start state it doesnt have parents so even if we start at the next key from the parent
        # we can't garuentee that the next state from the parent is in the path to get to the goal so start at the goal state and work backwards.

        while currentKey is not None:
            path.append(stateMap[currentKey]) # Get the actual version of the hashed version of the goal state so we get the nxn array
            currentKey = parents[currentKey]  # Which state generated the goal then make that the current key and keep going until we get to the start state which doesn't have parents
        
        path.reverse()
        return path

    @cache
    def depthFirstSearch(self) -> List[List[List[int]]]:
        stackOfStates: Deque[List[List[int]]] = deque()
        stackOfStates.append(self.startState)
        
        visited: Set[Tuple[int, ...]] = set()
        visited.add(self.startStateKey)

        parents: Dict[Tuple[int, ...], Optional[Tuple[int, ...]]] = {self.startStateKey: None}
        stateMap: Dict[Tuple[int, ...], List[List[int]]] = {self.startStateKey: self.startState}


        while stackOfStates:
            popedStates: List[List[int]] = stackOfStates.pop()
            popedStatesKey: Tuple[int, ...] = self.GameMachanics.flattenState(popedStates)

            if popedStatesKey == self.goalStateKey: break

            for sucessorStates in self.GameMachanics.generateSuccessorStates(popedStates):
                sucessorStatesKey: Tuple[int, ...] = self.GameMachanics.flattenState(sucessorStates)

                if sucessorStatesKey not in visited:
                    visited.add(sucessorStatesKey)
                    parents[sucessorStatesKey] = popedStatesKey
                    stateMap[sucessorStatesKey] = sucessorStates
                    
                    stackOfStates.append(sucessorStates)
        
        if self.goalStateKey not in parents: return []

        path: List[List[List[int]]] = []
        current: Optional[Tuple[int, ...]] = self.goalStateKey

        while current is not None:
            path.append(stateMap[current])
            current = parents[current]

        path.reverse()
        return path

    @cache
    def uniformCostingSearch(self) -> List[List[List[int]]]:
        minHeapOfStates: List[Tuple[int, List[List[int]]]] = []
        heapq.heappush(minHeapOfStates, (0, self.startState))

        visited: Set[Tuple[int, ...]] = set()
        visited.add(self.startStateKey)
        
        parents: Dict[Tuple[int, ...], Optional[Tuple[int, ...]]] = {self.startStateKey: None}
        stateMap: Dict[Tuple[int, ...], List[List[int]]] = {self.startStateKey: self.startState}

        while minHeapOfStates:
            popedHeapStates: Tuple[int, List[List[int]]] = heapq.heappop(minHeapOfStates)
            popedStatesKey: Tuple[int, ...] = self.GameMachanics.flattenState(popedHeapStates[1])

            if (popedStatesKey == self.goalStateKey): break

            for sucessorStaes in self.GameMachanics.generateSuccessorStates(popedHeapStates[1]):
                sucessorStaesKey: Tuple[int, ...] = self.GameMachanics.flattenState(sucessorStaes)
                costOfMovingToStates: int = self.GameMachanics.generateCost(popedHeapStates[1], sucessorStaes)

                if (sucessorStaesKey not in visited):
                    visited.add(sucessorStaesKey)
                    heapq.heappush(minHeapOfStates, (costOfMovingToStates + popedHeapStates[0], sucessorStaes))
                    parents[sucessorStaesKey] = popedStatesKey
                    stateMap[sucessorStaesKey] = sucessorStaes
        
        if self.goalStateKey not in parents: return []

        path: List[List[List[int]]] = []
        current: Optional[Tuple[int, ...]] = self.goalStateKey

        while current is not None:
            path.append(stateMap[current])
            current = parents[current]
        
        path.reverse()
        return path
    
    @cache
    def depthLimitedSearch(self, depth: int) -> List[List[List[int]]]:
        stackOfStates: Deque[Tuple[List[List[int]], int]] = deque()
        stackOfStates.append((self.startState, 0))
        
        visited: Set[Tuple[int, ...]] = set()
        visited.add(self.startStateKey)
        
        parents: Dict[Tuple[int, ...], Optional[Tuple[int, ...]]] = {self.startStateKey: None}
        stateMap: Dict[Tuple[int, ...], List[List[int]]] = {self.startStateKey: self.startState}

        count: int = 0
        while stackOfStates:
            popedState: Tuple[List[List[int]], int] = stackOfStates.pop()
            popedStateKey: Tuple[int, ...] = self.GameMachanics.flattenState(popedState[0])

            if ((popedStateKey == self.goalStateKey) or (popedState[1] >= depth)): continue

            for sucessorStates in self.GameMachanics.generateSuccessorStates(popedState[0]):
                sucessorStatesKey: Tuple[int, ...] = self.GameMachanics.flattenState(sucessorStates)

                if sucessorStatesKey not in visited:
                    visited.add(sucessorStatesKey)
                    stackOfStates.append((sucessorStates, popedState[1] + 1))
                    parents[sucessorStatesKey] = popedStateKey
                    stateMap[sucessorStatesKey] = sucessorStates

        if self.goalStateKey not in parents: return []

        current: Tuple[int, ...] = self.goalStateKey
        path: List[List[List[int]]] = []

        while current:
            path.append(stateMap[current])
            current = parents[current]
        
        path.reverse()

        return path
    
    @cache
    def itterativeDeepeningSearch(self, maxDepth: int) -> List[List[List[int]]]:
        for depth in range(0, maxDepth + 1):
            result: List[List[List[int]]] = self.depthLimitedSearch(depth)

            if result: return result
        
        return []
