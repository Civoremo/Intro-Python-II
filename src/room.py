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
        for i in self.items:
            if i == item:
                self.items.pop()

    def __str__(self):
        return (f'{self.location} -- {self.items}\n + {self.description}')
