from typing import Dict, List

class NimStandard:
    def __init__(self):
        self.gameState: Dict[str, int] = {"blue": 5,"red": 5}

    def generateSucessorStates(self, state: Dict[str, int]) -> List[Dict[str, int]]:
        sucessorStates: List[Dict[str, int]] = []

        if ((state["blue"] - 2) < 0): pass
        else: sucessorStates.append({"blue": state["blue"] - 2, "red": state["red"]})

        if ((state["red"] - 2) < 0): pass
        else: sucessorStates.append({"blue": state["blue"], "red": state["red"] - 2})

        if ((state["blue"] - 1) < 0): pass
        else: sucessorStates.append({"blue": state["blue"] - 1, "red": state["red"]})

        if ((state["red"] - 1) < 0): pass
        else: sucessorStates.append({"blue": state["blue"], "red": state["red"] - 1})

        return sucessorStates

    def minMaxTreeFull(self):
        pass

        
