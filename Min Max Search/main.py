from nim_standard import NimGameNonPruning
from typing import Dict, List

def main() -> int:
    print(NimGameNonPruning().generateSucessorStates({"blue": 0,"red": 5}))

    return 0

if __name__ == "__main__":
    main()