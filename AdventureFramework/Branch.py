class Branch:
    def __init__(self, outcome_text = None, next_event = None):
        self.outcome_text = outcome_text
        self.next_event = next_event

    #getters
    def get_outcome_text(self):
        return self.outcome_text
    
    def get_next_event(self):
        return self.next_event

    #setters
    def set_outcome_text(self, text):
        self.outcome_text = text

    def set_next_event(self, next_event):
        self.next_event = next_event

    #display
    def display_outcome_text(self):
        print(self.get_outcome_text)
    
    def display_next_event_name(self):
        print(self.get_next_event().get_story_text())

    


