# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, location, description, items):
        self.location = location
        self.description = description
        self.items = items

    def addItemToRoom(self, item):
        self.items.append(item)

    def removeItemFromRoom(self, item):
        for index, i in enumerate(self.items):
            if i == item:
                self.items.pop(index)

    def __str__(self):
        return (f'{self.location} -- {self.items}\n + {self.description}')

    def __repr__(self):
        return (f'{self.location} -- {self.items}\n + {self.description}')
