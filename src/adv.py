from room import Room
from player import Player
import Item

# Declare all available items

lamp = {'Lamp', 'An old forgoten lamp with some oil still remaining.'}
pouch = {'Pouch', 'Old, slightly torn pouch that; usefull for carrying things.'}
sword = {'Sword', 'Dull sword; good for smashing things.'}
coins = {'Coins', 'Unfamiliar coins, might still hold some value.'}
shard1 = {'ArtiBact', 'Blue in color. Looks to be a piece of a bigger puzzle.'}
shard2 = {'ArtiRact', 'Red in color. Looks to be a piece of a bigger puzzle.'}
shard3 = {'ArtiWact', 'White in color. Looks to be a piece of a bigger puzzle.'}
shield = {
    'Shield', 'Rotting piece of wood that may have been used as a shield in the past.'}
bow = {'Bow', 'Magnificently crafted bow; missing string to be functional!'}
arrows = {'Arrows', 'Deadly, pointy sticks.'}
jar = {'Jar', 'Empty jar; can hold things.'}
flower = {'Flower', 'A flower that grew out of stone.'}
mirror = {'Mirror', 'Antique mirror, looks valuable.'}
chalise = {'Chalise', 'A fancy cup to drink out of.'}
crown = {'Crown', 'Long lost crown of ...'}
ruby = {'Ruby', 'Precious stone; red I believe.'}
emerald = {'Emerald', 'Precious stone; green I think.'}
pebbles = {'Pebbles', 'No ordinary rocks, smooth edges.'}
slingshot = {'Slingshot', "Dennis the Menace's favorite weapon."}
slime = {'Slime', 'Mysterious smelling goo.'}

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

    'chamber': Room('Bed Chamber', """A finely furnished bed chamber, all the things 
are covered in dust and cob webs from years of neglect""", []),

    'cliff': Room('Cliff Edge', """Careful now, one small slip up and this could be the 
end of your adventure.""", []),

    'basement': Room('Pungent Basement', """Dark, cold, damp basement; gives me the creeps""", []),

    'dungeon': Room('Dungeon', """Torture devices are scattered throughout the room""", []),

    'armory': Room('Armory', """A large room that used to hold a stockpile of weapons 
but now it sits mostly empty""", []),

    'cellar': Room('Wine Cellar', 'All the bottles are smashed. What a shame.', []),

    'tunnel': Room('Long Corridor', 'Dark and narrow corridor, hard to see where it leads.' []),

    'fountain': Room('Fountain of Youth', 'Elegantly decorated fountain; ice cold water still gushing.' []),

    'alchemy': Room('Alchemy Chamber', """Elaborate contraptions scattered throughout the room 
accompanied by an unbearable stench.""", []),

    'stairway': Room('Winding Stairway', """Caution, uneven steps!""", []),

    'storage': Room('Storage Room', """Piles of junk knocked down on the floor""", []),

    'lavatory': Room('Lavatory', """Ocupado! sign tossed on the floor; doesn't 
look like it was cleaned any time recently""", []),

    'library': Room('Grand Library', 'Windows appear to be painted dark as to stop light from coming in', []),
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

room['narrow'].e_to = room['chamber']
room['chamber'].s_to = room['cliff']
room['chamber'].w_to = room['narrow']
room['cliff'].n_to = room['chamber']
room['treasure'].n_to = room['basement']
room['basement'].e_to = room['dungeon']
room['basement'].n_to = room['cellar']
room['basement'].s_to = room['treasure']
room['dungeon'].s_to = room['armory']
room['dungeon'].w_to = room['basement']
room['armory'].n_to = room['dungeon']
room['cellar'].w_to = room['tunnel']
room['cellar'].s_to = room['basement']
room['tunnel'].s_to = room['alchemy']
room['tunnel'].n_to = room['fountain']
room['tunnel'].w_to = room['stairway']
room['tunnel'].e_to = room['cellar']
room['fountain'].s_to = room['tunnel']
room['alchemy'].s_to = room['tunnel']
room['stairway'].s_to = room['storage']
room['stairway'].e_to = room['tunnel']
room['storage'].s_to = room['library']
room['storage'].w_to = room['lavatory']
room['storage'].n_to = room['stairway']
room['library'].n_to = room['storage']
room['library'].e_to = room['foyer']
room['foyer'].w_to = room['library']

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
            print('\n_-_-_- Walked North\n\n')
        elif currentPlayer.room == 'foyer':
            currentPlayer.room = 'overlook'
            print('\n_-_-_- Walked North\n\n')
        elif currentPlayer.room == 'narrow':
            currentPlayer.room = 'treasure'
            print('\n_-_-_- Walked North\n\n')
        else:
            print("\n--- Can't go that way! ---\n")
    if player_input == 's' or player_input == 'S':
        if currentPlayer.room == 'foyer':
            currentPlayer.room = 'outside'
            print('\n_-_-_- Walked South\n\n')
        elif currentPlayer.room == 'overlook':
            currentPlayer.room = 'foyer'
            print('\n_-_-_- Walked South\n\n')
        elif currentPlayer.room == 'treasure':
            currentPlayer.room = 'narrow'
            print('\n_-_-_- Walked South\n\n')
        else:
            print("\n--- Can't go that way! ---\n")
    if player_input == 'e' or player_input == 'E':
        if currentPlayer.room == 'foyer':
            currentPlayer.room = 'narrow'
            print('\n_-_-_- Walked East\n\n')
        else:
            print("\n--- Can't go that way! ---\n")
    if player_input == 'w' or player_input == 'W':
        if currentPlayer.room == 'narrow':
            currentPlayer.room = 'foyer'
            print('\n_-_-_- Walked West\n\n')
        else:
            print("\n--- Can't go that way! ---\n")


def available_directions():
    if currentPlayer.room == 'outside':
        print('-> [ N ] <-')
    if currentPlayer.room == 'foyer':
        print('-> [ N  S  E ] <-')
    if currentPlayer.room == 'overlook':
        print('-> [ S ] <-')
    if currentPlayer.room == 'narrow':
        print('-> [ N  W ] <-')
    if currentPlayer.room == 'treasure':
        print('-> [ S ] <-')


currentPlayer = Player('Johnny', 'outside')

print('\n\n')
print('====================================\n')
print('|          Pointless  Quest        |\n')
print('|        --------------------      |\n')
print('|              Q to quit           |\n')
print('====================================\n')

while True:
    for key, value in room.items():
        if currentPlayer.room == key:
            print(f'{value}')
    available_directions()
    cmd = input('\nEnter command -> ')
    player_movement(cmd)
    if cmd == 'q' or cmd == 'Q':
        print('\nGoodbye!')
        break
