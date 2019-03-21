from item import Item


class Treasure(Item):
    def __init__(self, name, description, value=0):
        self.value = value
        super().__init__(name, description)
