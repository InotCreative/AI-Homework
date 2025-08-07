from typing import Dict, List, Union, Tuple, Optional
import math

def evalFunction(state: Dict[str, Union[int, str]], standardGame: bool) -> int:
    if state["red"] == 0 or state["blue"] == 0: return 0

    score: int = (2 * int(state["red"])) + (3 * int(state["blue"]))

    return score if standardGame else -score

class GamePlay:
    def __init__(self, numberOfRedMarbles: int, numberOfBlueMarbles: int, firstPlayer: str, standardGame: bool) -> None:
        self.numberOfRedMarbles: int = numberOfRedMarbles
        self.numberOfBlueMarbles: int = numberOfBlueMarbles
        self.firstPlayer: str = firstPlayer
        self.initialState: Dict[str, Union[int, str]] = {"blue": self.numberOfBlueMarbles, "red": self.numberOfRedMarbles, "player": "root", "depth": 0}
        self.standardGame: bool = standardGame

    def parseHumanInput(self, previousState: Dict[str, Union[str, int]]) -> Tuple[Optional[Dict[str, Union[str, int]]], Optional[str]]:
        if self.isTerminalState(previousState): return (None, None)

        print("\033[34m\n" + '=' * 90)
        print("HUMAN TURN".center(90))
        print("=" * 90 + "\033[0m")

        states, actions = self.generateSuccessorStates(previousState)
        for index in range(0, len(actions)): print(f"\033[31m{index}.\033[0m {actions[index]}")

        while True:
            try:
                humanAction: int = int(input("\nCHOOSE ACTION \033[31m(INT): \033[0m"))
                
                if 0 <= humanAction < len(actions): break
                else: print("Invalid action. Try again.")
            except ValueError:
                print("Invalid input. Enter an integer.")

        print(actions[humanAction])
        states[humanAction]["player"] = "human"

        return (states[humanAction], actions[humanAction])

    def generateSuccessorStates(self, state: Dict[str, Union[int, str]]) -> Tuple[List[Dict[str, Union[int, str]]], List[str]]:
        successorStates: List[List[Dict[str, Union[int, str]]], List[str]] = [[], []]
        nextPlayer: str = ""
        
        if state["player"] == "root": nextPlayer = self.firstPlayer
        elif state["player"] == "computer": nextPlayer = "human"
        elif state["player"] == "human": nextPlayer = "computer"
        
        if int(state["blue"]) - 2 >= 0:
            successorStates[0].append({"blue": int(state["blue"]) - 2, "red": int(state["red"]), "player": nextPlayer, "depth": int(state["depth"]) + 1})
            successorStates[1].append("Pick 2 blue marble")
        if int(state["red"]) - 2 >= 0:
            successorStates[0].append({"blue": int(state["blue"]), "red": int(state["red"]) - 2, "player": nextPlayer, "depth": int(state["depth"]) + 1})
            successorStates[1].append("Pick 2 red marble")
        if int(state["blue"]) - 1 >= 0:
            successorStates[0].append({"blue": int(state["blue"]) - 1, "red": int(state["red"]), "player": nextPlayer, "depth": int(state["depth"]) + 1})
            successorStates[1].append("Pick 1 blue marble")
        if int(state["red"]) - 1 >= 0:
            successorStates[0].append({"blue": int(state["blue"]), "red": int(state["red"]) - 1, "player": nextPlayer, "depth": int(state["depth"]) + 1})
            successorStates[1].append("Pick 1 red marble")
        
        return (successorStates[0], successorStates[1])

    def isTerminalState(self, state: Dict[str, Union[int, str]]) -> bool:
        if int(state["red"]) == 0 or int(state["blue"]) == 0: return True
        if len(self.generateSuccessorStates(state)[0]) == 0: return True
        
        return False

    def utilityFunction(self, state: Dict[str, Union[int, str]]) -> int:
        if (self.isTerminalState(state) == True):
            score: int = (2 * int(state["red"])) + (3 * int(state["blue"]))

            if (state["player"] == "computer"):
                if (self.standardGame == True): return -score
                else: return score
            else:
                if (self.standardGame): return score
                else: return -score

class Nim:
    def __init__(self, numberOfRedMarbles: int, numberOfBlueMarbles: int, firstPlayer: str, standardGame: bool) -> None:
        self.numberOfRedMarbles: int = numberOfRedMarbles
        self.numberOfBlueMarbles: int = numberOfBlueMarbles
        self.firstPlayer: str = firstPlayer
        self.gamePlay: GamePlay = GamePlay(numberOfRedMarbles=numberOfRedMarbles, numberOfBlueMarbles=numberOfBlueMarbles, firstPlayer=firstPlayer, standardGame=standardGame)
        self.standardGame: bool = standardGame
    
    def getMoveOrder(self) -> List[int]:
        '''
        For standard version: [1, 0, 3, 2] corresponds to:
        1: Pick 2 red marble
        0: Pick 2 blue marble
        3: Pick 1 red marble
        2: Pick 1 blue marble
        For misère version, invert the order: [2, 3, 0, 1]
        '''

        return [2, 3, 0, 1] if not self.standardGame else [1, 0, 3, 2]
    
    def maxPlayer(self, state: Dict[str, Union[int, str]], alpha: float, beta: float) -> int:
        if self.gamePlay.isTerminalState(state): 
            return self.gamePlay.utilityFunction(state)
        
        value: float = -math.inf
        successorStates, actions = self.gamePlay.generateSuccessorStates(state)
        order = self.getMoveOrder()
        
        for idx in order:
            if idx < len(successorStates):
                value = max(value, self.minPlayer(successorStates[idx], alpha, beta))
                
                if value >= beta: return value
                
                alpha = max(alpha, value)
        
        return value
    
    def minPlayer(self, state: Dict[str, Union[int, str]], alpha: float, beta: float) -> int:
        if self.gamePlay.isTerminalState(state): 
            return self.gamePlay.utilityFunction(state)
        
        value: float = math.inf
        successorStates, actions = self.gamePlay.generateSuccessorStates(state)
        order = self.getMoveOrder()
        
        for idx in order:
            if idx < len(successorStates):
                value = min(value, self.maxPlayer(successorStates[idx], alpha, beta))
                    
                if value <= alpha: return value
                    
                beta = min(beta, value)
        
        return value
    
    def bestMove(self, state: Dict[str, Union[int, str]]) -> Tuple[Dict[str, Union[int, str]], str]:
        successorStates, actions = self.gamePlay.generateSuccessorStates(state)
        bestValue: float = -math.inf
        bestIdx: int = 0
        order = self.getMoveOrder()
        
        for idx in order:
            if idx < len(successorStates):
                value: int = self.minPlayer(successorStates[idx], -math.inf, math.inf)
                    
                if value > bestValue:
                    bestValue = value
                    bestIdx = idx
        
        return successorStates[bestIdx], actions[bestIdx]

class NimWithDepth(Nim):
    def __init__(self, numberOfRedMarbles: int, numberOfBlueMarbles: int, firstPlayer: str, standardGame: bool, depth: Optional[int] = None) -> None:
        super().__init__(numberOfRedMarbles, numberOfBlueMarbles, firstPlayer, standardGame)
        self.depth: Optional[int] = depth
        self.standardGame: bool = standardGame
    
    def maxPlayer(self, state: Dict[str, Union[int, str]], alpha: float, beta: float) -> int:
        if self.gamePlay.isTerminalState(state):  return self.gamePlay.utilityFunction(state)
        
        if self.depth is not None and int(state["depth"]) >= self.depth: return evalFunction(state, self.standardGame)
            
        value: float = -math.inf
        successorStates, actions = self.gamePlay.generateSuccessorStates(state)
        order: List[int] = super().getMoveOrder()

        for idx in order:            
            value = max(value, self.minPlayer(successorStates[idx], alpha, beta))
            
            if value >= beta: return value
            
            alpha = max(alpha, value)

        return value

    def minPlayer(self, state: Dict[str, Union[int, str]], alpha: float, beta: float) -> int:
        if self.gamePlay.isTerminalState(state): return self.gamePlay.utilityFunction(state)
        
        if self.depth is not None and int(state["depth"]) >= self.depth: return evalFunction(state, self.standardGame)
            
        value: float = math.inf
        successorStates, actions = self.gamePlay.generateSuccessorStates(state)
        order: List[int] = super().getMoveOrder()
        
        for idx in order:            
            value = min(value, self.maxPlayer(successorStates[idx], alpha, beta))
            
            if value <= alpha: return value
            
            beta = min(beta, value)
        
        return value

    def bestMove(self, state: Dict[str, Union[int, str]]) -> Tuple[Dict[str, Union[int, str]], str]:
        successorStates, actions = self.gamePlay.generateSuccessorStates(state)
        bestValue: float = -math.inf
        bestIdx: int = 0
        order: List[int] = [2, 3, 0, 1] if not self.standardGame else [1, 0, 3, 2]
        
        for idx in order:            
            value: int = self.minPlayer(successorStates[idx], -math.inf, math.inf)
            
            if value > bestValue:
                bestValue = value
                bestIdx = idx
        
        return successorStates[bestIdx], actions[bestIdx]

class RedBlueNimGame:
    def __init__(self, numberOfRedMarbles: int, numberOfBlueMarbles: int, standardGame: bool, firstPlayer: str, depth: Optional[int]) -> None:
        self.numberOfRedMarbles: int = numberOfRedMarbles
        self.numberOfBlueMarbles: int = numberOfBlueMarbles
        self.standardGame: bool = standardGame
        self.firstPlayer: str = firstPlayer
        self.depth: Optional[int] = depth
        self.state: Dict[str, Union[int, str]] = {"red": numberOfRedMarbles, "blue": numberOfBlueMarbles, "player": "root", "depth": 0}
        self.currentPlayer: str = firstPlayer
        self.nim: Union[Nim, NimWithDepth] = None

        if depth is None: self.nim = Nim(numberOfRedMarbles, numberOfBlueMarbles, firstPlayer, standardGame)
        else: self.nim = NimWithDepth(numberOfRedMarbles, numberOfBlueMarbles, firstPlayer, standardGame, depth)

    def startGame(self) -> None:
        print(f"Starting Red-Blue Nim: {self.numberOfRedMarbles} red, {self.numberOfBlueMarbles} blue, {'standard' if self.standardGame else 'misère'} version, {self.firstPlayer} goes first" + (f", depth limit {self.depth}" if self.depth else ""))
        
        while True:
            if self.nim.gamePlay.isTerminalState(self.state):
                print("\n" + "\033[91m=" * 90)
                print("GAME OVER".center(90))
                print("=" * 90 + "\033[0m")
                score: int = 2 * int(self.state["red"]) + 3 * int(self.state["blue"])
                
                if self.standardGame: winner: str = "human" if self.state["player"] == "human" else "computer"
                else: winner: str = "computer" if self.state["player"] == "human" else "human"
                
                print(f"Winner: {winner}")
                print(f"Final score: {score} points {'won' if winner == 'computer' else 'lost'} by computer.")
                break

            if self.currentPlayer == "computer":
                print("\n\033[31m" + "=" * 90)
                print("COMPUTER TURN".center(90))
                print("=" * 90 + "\033[0m")

                nextState, action = self.nim.bestMove(self.state)
                
                print(f"Computer chooses: {action}")
                nextState["player"] = "computer"
                
                self.state = nextState
                self.currentPlayer = "human"
            else:
                nextState, action = self.nim.gamePlay.parseHumanInput(self.state)
                
                if nextState is None: continue
                
                nextState["player"] = "human"
                
                self.state = nextState
                self.currentPlayer = "computer"

