from .BranchGroup import BranchGroup

class BranchGroupCheck(BranchGroup):
    def __init__(self, name, branches = [], game_roll_modifier = 0):
        self.name = name
        self.branches = branches
        self.game_roll_modifier = game_roll_modifier
