from file_handle import FileHandle

def main():
    startState: list[list[int]] = FileHandle("start.txt").populateStateArray()
    goalState: list[list[int]] = FileHandle("goal.txt").populateStateArray()

    print(startState)
    print(goalState)

if __name__ == "__main__":
    main()