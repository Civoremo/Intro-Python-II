from item import Item

class Weapon(Item):
    def __init__(self, name, description, attack_points):
        self.name = name
        self.description = description
        self.attack_points = attack_points
