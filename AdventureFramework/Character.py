class Character:
    def __init__(self, name = 'The Boss', attributable_points = 10, attribute_list = []):
        self.name = name
        self.attributable_points = attributable_points
        self.attribute_list = attribute_list
        self.attribute_dict = {attribute: 0 for attribute in attribute_list}