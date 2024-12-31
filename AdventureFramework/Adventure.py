from .Character import Character

class Adventure:
    """
    Ultimately, we will 'attach' other class instances to this--adventure will have a spot for character, events, etc. Basically
    use a simple list to create a basica container for events inside the adventure instance. Then have methods in the
    adventure class like add_event, add_character, etc

    I've added an npcs dictionary and each npc will be implemented as a character so the user can easily use npc attributes in various checks. There will
    be no additional functionaliy like npc choices, opinions, or sentiment. This is purely to make the modifiers passed more consistent.
    """
    #Constructor
    def __init__(self, name, attributes = [], current_event = None, previous_event = None, journey_complete = False, main_character = None, npcs = None):
        self.current_event = current_event
        self.name = name
        self.attributes = attributes
        self.current_event = current_event
        self.previous_event = previous_event
        self.journey_complete = journey_complete
        self.npcs = npcs

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

    def set_main_character(self, name):
        self.main_character = Character(name, attribute_list = self.get_attributes())
    
    def set_main_character_attribute(self, attribute, value):
        if attribute in self.main_character.attribute_dict:
            self.main_character.attribute_dict[attribute] = value
        else:
            raise ValueError(f"Attribute '{attribute}' does not exist for the main character.")

        