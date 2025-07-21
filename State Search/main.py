from uninformed_search import UninformedSearch
from informed_search import InformedSearch
from game_machenics import GameMachanics
from file_handle import FileHandle
from typing import List
import sys
import time

def banner():
    print("\033[96m" + "=" * 60)
    print("🧠 AI Puzzle Solver CLI".center(60))
    print("=" * 60 + "\033[0m")

def printHelp():
    print("""
\033[93mUsage:\033[0m
    python main.py <type> <algorithm> [depth]

\033[93mTypes:\033[0m
    us  - Uninformed Search
    is  - Informed Search

\033[93mAlgorithms:\033[0m
    us: bfs | dfs | ucs | dls <depth> | ids <depth>
    is: gs  | as

\033[93mExample:\033[0m
    python main.py us bfs
    python main.py us dls 3
    python main.py is as
""")

def main():
    banner()

    if len(sys.argv) < 3:
        printHelp()
        return

    search_type = sys.argv[1].lower()
    algorithm = sys.argv[2].lower()
    depth = int(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3].isdigit() else None

    try:
        startState: List[List[List[int]], int] = FileHandle("start.txt").fileRead()
        goalState: List[List[List[int]], int] = FileHandle("goal.txt").fileRead()
    except Exception as e:
        print(f"\033[91mError reading files: {e}\033[0m")
        return

    start_time = time.time()

    try:
        if search_type == "is":
            search = InformedSearch(startState[0], goalState[0], startState[1])
            if algorithm == "gs":
                result = search.greedySearch()
            elif algorithm == "as":
                result = search.aStarSearch()
            else:
                raise ValueError("Supported informed algorithms: gs, as")

        elif search_type == "us":
            search = UninformedSearch(startState[0], goalState[0], startState[1])
            if algorithm == "bfs":
                result = search.bredthFirstSearch()
            elif algorithm == "dfs":
                result = search.depthFirstSearch()
            elif algorithm == "ucs":
                result = search.uniformCostingSearch()
            elif algorithm == "dls":
                if depth is None:
                    raise ValueError("DLS requires depth argument.")
                result = search.depthLimitedSearch(depth)
            elif algorithm == "ids":
                if depth is None:
                    raise ValueError("IDS requires depth argument.")
                result = search.itterativeDeepeningSearch(depth)
            else:
                raise ValueError("Unsupported uninformed algorithm.")
        else:
            raise ValueError("Search type must be 'us' or 'is'.")

        GameMachanics(startState[1]).printMoves(result)
        elapsed = time.time() - start_time
        print(f"\n\033[92m✔️ Completed in {elapsed:.4f} seconds.\033[0m")

    except Exception as e:
        print(f"\033[91mError: {e}\033[0m")
        printHelp()

if __name__ == "__main__":
    main()
