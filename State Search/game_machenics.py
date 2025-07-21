import copy

class GameMachanics:
    def __init__(self, n: int):
        self.n: int = n

    def flattenState(self, stateToFlatten: list[list[int]]) -> tuple[int, ...]:
        flattenedState = []

        for row in range(0, len(stateToFlatten)):
            for collum in range(0, len(stateToFlatten[row])):
                flattenedState.append(stateToFlatten[row][collum])
        
        return tuple(flattenedState)
    
    def findBlankPosition(self, state: list[list[int]]) -> tuple[int, int]:
        for row in range(0, len(state)):
            for collum in range(0, len(state[row])):
                if (state[row][collum] == 0): return (row, collum)
    
    def findPossibleMoves(self, state) -> list[str]:
        x, y = self.findBlankPosition(state)
        moves: list[str] = []

        if (x > 0): moves.append("up")
        if (x < self.n - 1): moves.append("down")
        if (y > 0): moves.append("left")
        if (y < self.n - 1): moves.append("right")

        return moves

    def generateSuccessorStates(self, state: list[list[int]]) -> list[list[list[int]]]:
        
        possibleMoves: list[str] = self.findPossibleMoves(state)
        
        successorStates: list[list[list[int]]] = []
        x, y = self.findBlankPosition(state)

        for move in possibleMoves:
            if (move == "up"):
                stateCopy = copy.deepcopy(state)

                stateCopy[x - 1][y] = stateCopy[x][y]
                stateCopy[x][y] = state[x - 1][y]
                
                successorStates.append(stateCopy)

            elif (move == "down"):
                stateCopy = copy.deepcopy(state)

                stateCopy[x + 1][y] = stateCopy[x][y]
                stateCopy[x][y] = state[x + 1][y]
                
                successorStates.append(stateCopy)

            elif (move == "left"):
                stateCopy = copy.deepcopy(state)
                
                stateCopy[x][y - 1] = stateCopy[x][y]
                stateCopy[x][y] = state[x][y - 1]
                
                successorStates.append(stateCopy)

            elif (move == "right"):
                stateCopy = copy.deepcopy(state)
                
                stateCopy[x][y + 1] = stateCopy[x][y]
                stateCopy[x][y] = state[x][y + 1]

                successorStates.append(stateCopy)
        
        return successorStates

    def printMoves(self, path: list[list[list[int]]]) -> None:
        if (len(path) == 0): print("NO PATH FOUND!")

        for move in range(0, len(path)):
            print(f"=== MOVE {move} ===")
            
            for x in path[move]:
                print(x, end="\n")
            
            print("\n")
    
    def generateCost(self, toState: list[list[int]], fromStates: list[list[int]]) -> int:
        toStateBlankX, toStateBlankY = self.findBlankPosition(toState)
        fromStateBlankX, fromStateBlankY = self.findBlankPosition(fromStates)
        
        return fromStates[toStateBlankX][toStateBlankY]