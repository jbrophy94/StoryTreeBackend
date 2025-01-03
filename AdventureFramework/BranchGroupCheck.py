from .BranchGroup import BranchGroup
"""
This will incorporate rolling/attributes into the outcome of the user's choice. 
"""
class BranchGroupCheck(BranchGroup):
    def __init__(self, name, branches = [], game_roll_modifier = 0):
        self.name = name
        self.branches = branches
        self.game_roll_modifier = game_roll_modifier
