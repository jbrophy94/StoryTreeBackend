class Adventure:
    """Ultimately, we will 'attach' other class instances to this--adventure will have a spot for character, events, etc. Basically
    use a simple list to create a basica container for events inside the adventure instance. Then have methods in the
    adventure class like add_event, add_character, etc"""
    #Constructor
    def __init__(self, name, attributes = [], current_event = None, previous_event = None, journey_complete = False):
        self.current_event = current_event
        self.name = name
        self.attributes = attributes
        self.current_event = current_event
        self.previous_event = previous_event
        self.journey_complete = journey_complete

    #getters
    def get_name(self):
        return self.name
    
    def get_attributes(self):
        return self.attributes
    
    def get_current_event(self):
        return self.current_event
    
    def get_previous_event(self):
        return self.previous_event
    
    def get_journey_complete(self):
        return self.journey_complete
    
    #setters
    def set_name(self, name):
        self.name = name

        #still need to add removal functionality
    def add_attribute(self, attribute):
        self.attributes.append(attribute)
    
    def set_current_event(self, current_event):
        self.current_event = current_event
    
    def set_previous_event(self, previous_event):
        self.previous_event = previous_event

    #Attachment setters
    #set_character 
    """alternatively we could do set_player_character if we want to build more characters 
    into the story directly as character objects, but for now lets implement this simply"""

    #attach_event

    