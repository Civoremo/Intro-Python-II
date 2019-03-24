from item import Item

class Potion(Item):
    def __init__(self, name, description, action=2):
        self.action = action
        super().__init__(name, description)