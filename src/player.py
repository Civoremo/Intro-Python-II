# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room):
        self.room = room

    def __str__(self):
        return f'Your location: "{self.room}"'

    def __repr__(self):
        return f"Your location: '{self.room}'"
