from game_machenics import GameMachanics
from collections import deque
import heapq
from typing import List, Tuple, Optional, Dict, Set, Deque

class InformedSearch:
    def __init__(self, startState: List[List[int]], goalState: List[List[int]], n: int) -> None:
        self.startState: List[List[int]]    = startState
        self.goalState: List[List[int]]     = goalState
        self.n                              = n
        self.GameMachanics: GameMachanics   = GameMachanics(self.n)
        self.startStateKey: Tuple[int, ...] = self.GameMachanics.flattenState(self.startState)
        self.goalStateKey: Tuple[int, ...]  = self.GameMachanics.flattenState(self.goalState)

    def costToGoalHurestic(self, currentState: List[List[int]]) -> int:
        pass
    def greedySearch(self):
        pass
    def aStarSearch(self):
        pass