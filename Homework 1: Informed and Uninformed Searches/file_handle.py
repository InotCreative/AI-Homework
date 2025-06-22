class FileHandle:
    def __init__(self, fileName: str):
        self.fileName: str = fileName
    
    def populateStateArray(self) -> list[list[int]]:
        stateArray: list[list[int]] = []

        with open(self.fileName, "r") as inputFile:
            for fileLine in inputFile:
                line = fileLine.strip()

                if line == "END OF FILE": break

                if line:
                    intFileLine = [int(x) for x in line.split()]
                    stateArray.append(intFileLine)
        
        return stateArray