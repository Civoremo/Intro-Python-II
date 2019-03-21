# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, location, items):
        self.name = name
        self.location = location
        self.items = items

    def addItemToUser(self, item):
        self.items.append(item)

    def removeItemFromUser(self, item):
        for index, i in enumerate(self.items):
            if i == item:
                self.items.pop(index)

    def __str__(self):
        return f'Your location: "{self.location}"'

    def __repr__(self):
        return f"Your location: '{self.location}'"
