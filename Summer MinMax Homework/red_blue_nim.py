import sys
import textwrap
from typing import Dict, Union, List, Optional
from nim import RedBlueNimGame
import os

def main() -> int:
    os.system("clear" if os.name == "posix" else "cls")
    
    print("\033[34m" + "=" * 90)
    print("🧠 GAME PLAYING PROBLEM: MIN-MAX SEARCH FOR NIM CLI".center(90))
    print("=" * 90 + "\033[0m")

    if len(sys.argv) < 3:
        help: str = """
        \033[93mUsage:\033[0m
            python3 red_blue_nim <num-red> <num-blue> [<version>] [<first-player>] [-d <depth>]

        \033[93mArguments:\033[0m
            \033[96m<num-red>\033[0m:   Number of red marbles (required)
            \033[96m<num-blue>\033[0m:  Number of blue marbles (required)

        \033[93mOptional Flags:\033[0m
            \033[96m-m\033[0m                  Use misère version (player \033[1mwins\033[0m if a pile is empty on their turn)
                                Default is standard version (player \033[1mloses\033[0m if a pile is empty on their turn)

            \033[96m-h\033[0m                  Human plays first
                                Default is computer plays first

            \033[96m-d <depth>\033[0m          Use depth-limited MinMax (for extra credit)

        \033[93mGameplay:\033[0m
            - Computer uses MinMax with Alpha-Beta pruning to choose moves
            - Human is prompted to enter a move on their turn
            - Turns alternate until either pile is empty

        \033[93mExample:\033[0m
            python3 red_blue_nim 3 4 -m -h -d 4
        """

        print(textwrap.dedent(help))
        return 1

    numRed: int = int(sys.argv[1])
    numBlue: int = int(sys.argv[2])
    standardGame: bool = True
    firstPlayer: str = "computer"
    depth: Optional[int] = None
    i: int = 3

    while i < len(sys.argv):
        arg: str = sys.argv[i]
        
        if arg == "-m": standardGame = False
        elif arg == "-h": firstPlayer = "human"
        elif arg == "-d":
            if i + 1 < len(sys.argv):
                depth = int(sys.argv[i + 1])
                i += 1

        i += 1

    game: RedBlueNimGame = RedBlueNimGame(numRed, numBlue, standardGame, firstPlayer, depth)
    game.startGame()

    return 0

if __name__ == "__main__":
    sys.exit(main())
