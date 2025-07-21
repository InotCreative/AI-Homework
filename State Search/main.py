from uninformed_search import UninformedSearch
from informed_search import InformedSearch
from game_machenics import GameMachanics
from file_handle import FileHandle
from typing import List
import time

def main():
    startState: List[List[List[int]], int] = FileHandle("start.txt").fileRead()
    goalState: List[List[List[int]], int] = FileHandle("goal.txt").fileRead()

    GameMachanics(startState[1]).printMoves(UninformedSearch(startState[0], goalState[0], startState[1]).uniformCostingSearch())
    
if __name__ == "__main__":
    main()