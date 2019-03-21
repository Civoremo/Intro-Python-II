# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, location, description, items, is_light=False):
        self.location = location
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.is_light = is_light

    def __str__(self):
        return (f'{self.location} -- {self.items}\n + {self.description}')

    def __repr__(self):
        return (f'{self.location} -- {self.items}\n + {self.description}')

    def addItemToRoom(self, item):
        self.items.append(item)

    def removeItemFromRoom(self, item):
        for index, i in enumerate(self.items):
            if i == item:
                self.items.pop(index)

    def get_new_location(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None

    def available_exits(self):
        exits = []
        if self.n_to is not None:
            exits.append('N')
        if self.e_to is not None:
            exits.append('E')
        if self.s_to is not None:
            exits.append('S')
        if self.w_to is not None:
            exits.append('W')
        return ", ".join(exits)
