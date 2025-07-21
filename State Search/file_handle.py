from typing import List, Tuple
import os

class FileHandle:
    def __init__(self, filePath: str):
        self.filePath: str = filePath
    
    def fileRead(self) -> Tuple[List[List[int]], int]:
        self.filePath = os.path.normpath(self.filePath)
        gameGrid: List[List[int]] = []

        with open(self.filePath) as inputFile:
            for fileLines in inputFile:
                if (fileLines.strip() == "END OF FILE"): break

                tokens: List[str] = fileLines.split()
                tokens = [int(x) for x in tokens]

                gameGrid.append(tokens)
        
        return [gameGrid, len(gameGrid)]