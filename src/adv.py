from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.", ["Torch", "String"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["Chalise", "Coins"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ["Shield"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ["Arrows", "Bow"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ["Chest"]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def player_movement(player_input):
    if player_input == 'n' or player_input == 'N':
        if currentPlayer.room == 'outside':
            currentPlayer.room = 'foyer'
        elif currentPlayer.room == 'foyer':
            currentPlayer.room = 'overlook'
        elif currentPlayer.room == 'narrow':
            currentPlayer.room = 'treasure'
        else:
            print("Cant't go that way!")
    if player_input == 's' or player_input == 'S':
        if currentPlayer.room == 'foyer':
            currentPlayer.room = 'outside'
        elif currentPlayer.room == 'overlook':
            currentPlayer.room = 'foyer'
        elif currentPlayer.room == 'treasure':
            currentPlayer.room = 'narrow'
        else:
            print("Can't go that way!")
    if player_input == 'e' or player_input == 'E':
        if currentPlayer.room == 'foyer':
            currentPlayer.room = 'narrow'
        else:
            print("Can't go that way!")
    if player_input == 'w' or player_input == 'W':
        if currentPlayer.room == 'narrow':
            currentPlayer.room = 'foyer'
        else:
            print("Can't go that way!")


def available_directions():
    if currentPlayer.room == 'outside':
        print('Directions Available: [ N ]')
    if currentPlayer.room == 'foyer':
        print('Directions Available: [ N  S  E ]')
    if currentPlayer.room == 'overlook':
        print('Directions Available: [ S ]')
    if currentPlayer.room == 'narrow':
        print('Directions Available: [ N  W ]')
    if currentPlayer.room == 'treasure':
        print('Directions Available: [ S ]')


currentPlayer = Player('Johnny', 'outside')

print('\n\n')
print('====================================\n')
print('|          Pointless  Quest        |\n')
print('|        --------------------      |\n')
print('|              Q to quit           |\n')
print('====================================\n')

while True:
    # print(f'{currentPlayer.__str__()}')
    print(currentPlayer)
    for key, value in room.items():
        if currentPlayer.room == key:
            print(f'Location info: {value}')
    available_directions()
    cmd = input('\nEnter command -> ')
    player_movement(cmd)
    if cmd == 'q' or cmd == 'Q':
        print('Goodbye!')
        break
