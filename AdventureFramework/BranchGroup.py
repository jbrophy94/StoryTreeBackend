class BranchGroup:
    #This is a basic decision that does not include rolls or checks
    def __init__(self, name, branches = []):
        self.name = name
        self.branches = branches