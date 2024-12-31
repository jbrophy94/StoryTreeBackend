class Event:
    #An event will hold the story, choices, potential outcomes, and associated functionality
    def __init__(self, name = '',  story_text = '', branch_groups = []):
        self.name = name
        self.story_text = story_text
        self.branch_groups = branch_groups

    #getters
    def get_name(self):
        return self.name
    
    def get_story_text(self):
        return self.story_text
    
        #full list
    def get_branch_groups(self):
        return self.branch_groups
    
        #single branch group by index
    def get_branch_group(self, index):
        return self.branch_groups[index]
    

    #setters
    def set_name(self, name):
        self.name = name

    def set_story_text(self, text):
        self.story_text = text
    
        #still need to add removal functionality
    def add_branch_group(self, group):
        self.branch_groups.append(group)

    #display
    def display_story_text(self):
        print(self.get_story_text())

    
