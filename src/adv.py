from room import Room
from player import Player
from item import Item
from colorama import init, Fore, Back, Style
init(convert=True)

# Declare all available items

item = {
    'lamp': Item('Lamp', 'An old forgoten lamp with some oil still remaining.'),
    'pouch': Item('Pouch', 'Old, slightly torn pouch, usefull for carrying things.'),
    'sword': Item('Sword', 'Dull sword; good for smashing things.'),
    'coins': Item('Coins', 'Unfamiliar coins, might still hold some value.'),
    'shard1': Item('ArtiBact', 'Blue in color. Looks to be a piece of a bigger puzzle.'),
    'shard2': Item('ArtiRact', 'Red in color. Looks to be a piece of a bigger puzzle.'),
    'shard3': Item('ArtiWact', 'White in color. Looks to be a piece of a bigger puzzle.'),
    'shield': Item(
        'Shield', 'Rotting piece of wood that may have been used as a shield in the past.'),
    'bow': Item('Bow', 'Magnificently crafted bow; missing string to be functional!'),
    'arrows': Item('Arrows', 'Deadly, pointy sticks.'),
    'jar': Item('Jar', 'Empty jar; can hold things.'),
    'flower': Item('Flower', 'A flower that grew out of stone.'),
    'mirror': Item('Mirror', 'Antique mirror, looks valuable.'),
    'chalise': Item('Chalise', 'A fancy cup to drink out of.'),
    'crown': Item('Crown', 'Long lost crown of ...'),
    'ruby': Item('Ruby', 'Precious stone; red I believe.'),
    'emerald': Item('Emerald', 'Precious stone; green I think.'),
    'pebbles': Item('Pebbles', 'No ordinary rocks, smooth edges.'),
    'slingshot': Item('Slingshot', "Dennis the Menace's favorite weapon."),
    'slime': Item('Slime', 'Mysterious smelling goo.'),
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [item['lamp']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [item['flower'], item['shard1']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [item['slime']]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [item['shard3'], item['pouch']]),

    'chamber': Room('Bed Chamber', """A finely furnished bed chamber, all the things
are covered in dust and cob webs from years of neglect""", [item['mirror']]),

    'cliff': Room('Cliff Edge', """Careful now, one small slip up and this could be the
end of your adventure.""", [item['flower']]),

    'basement': Room('Pungent Basement', """Dark, cold, damp basement; gives me the creeps""", [item['sword']]),

    'dungeon': Room('Dungeon', """Torture devices are scattered throughout the room""", [item['shard2']]),

    'armory': Room('Armory', """A large room that used to hold a stockpile of weapons
but now it sits mostly empty""", [item['bow'], item['arrows']]),

    'cellar': Room('Wine Cellar', 'All the bottles are smashed. What a shame.', [item['shield']]),

    'tunnel': Room('Long Corridor', 'Dark and narrow corridor, hard to see where it leads.', [item['slingshot']]),

    'fountain': Room('Fountain of Youth', 'Elegantly decorated fountain; ice cold water still gushing.', [item['emerald'], item['ruby']]),

    'alchemy': Room('Alchemy Chamber', """Elaborate contraptions scattered throughout the room
accompanied by an unbearable stench.""", [item['jar'], item['coins']]),

    'stairway': Room('Winding Stairway', """Caution, uneven steps!""", [item['pebbles']]),

    'storage': Room('Storage Room', """Piles of junk knocked down on the floor""", []),

    'lavatory': Room('Lavatory', """Ocupado! sign tossed on the floor; doesn't
look like it was cleaned any time recently""", [item['crown']]),

    'library': Room('Grand Library', 'Windows appear to be painted dark as to stop light from coming in', [item['chalise']]),
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
room['alchemy'].n_to = room['tunnel']
room['stairway'].s_to = room['storage']
room['stairway'].e_to = room['tunnel']
room['storage'].s_to = room['library']
room['storage'].w_to = room['lavatory']
room['lavatory'].e_to = room['storage']
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
    global location
    global locationItems
    try:
        if player_input == 'n' or player_input == 'N':
            location = location.n_to
            locationItems = []
            print(Fore.YELLOW + '\n\n_-_-_-' +
                  Style.RESET_ALL + ' Walked North\n')
        elif player_input == 's' or player_input == 'S':
            location = location.s_to
            locationItems = []
            print('\n_-_-_- Walked South\n\n')
        elif player_input == 'e' or player_input == 'E':
            location = location.e_to
            locationItems = []
            print('\n_-_-_- Walked East\n\n')
        elif player_input == 'w' or player_input == 'W':
            location = location.w_to
            locationItems = []
            print('\n_-_-_- Walked West\n\n')
    except:
        print('\nNot a valid command, Try Again!\n')


def available_directions():
    global location
    if location.location == 'Outside Cave Entrance':
        print(Fore.RED + '-> [ N ] <-' + Style.RESET_ALL)
    if location.location == 'Foyer':
        print(Fore.RED + '-> [ N  E  S  W ] <-' + Style.RESET_ALL)
    if location.location == 'Grand Overlook':
        print(Fore.RED + '-> [ S ] <-' + Style.RESET_ALL)
    if location.location == 'Narrow Passage':
        print(Fore.RED + '-> [ N  E  W ] <-' + Style.RESET_ALL)
    if location.location == 'Treasure Chamber':
        print(Fore.RED + '-> [ N  S ] <-' + Style.RESET_ALL)
    if location.location == 'Bed Chamber':
        print(Fore.RED + '-> [ W  S ] <-' + Style.RESET_ALL)
    if location.location == 'Cliff Edge':
        print(Fore.RED + '-> [ N ] <-' + Style.RESET_ALL)
    if location.location == 'Pungent Basement':
        print(Fore.RED + '-> [ N  E  S ] <-' + Style.RESET_ALL)
    if location.location == 'Dungeon':
        print(Fore.RED + '-> [ W  S ] <-' + Style.RESET_ALL)
    if location.location == 'Armory':
        print(Fore.RED + '-> [ N ] <-' + Style.RESET_ALL)
    if location.location == 'Wine Cellar':
        print(Fore.RED + '-> [ W  S ] <-' + Style.RESET_ALL)
    if location.location == 'Long Corridor':
        print(Fore.RED + '-> [ N  E  S  W ] <-' + Style.RESET_ALL)
    if location.location == 'Fountain of Youth':
        print(Fore.RED + '-> [ S ] <-' + Style.RESET_ALL)
    if location.location == 'Alchemy Chamber':
        print(Fore.RED + '-> [ N ] <-' + Style.RESET_ALL)
    if location.location == 'Winding Stairway':
        print(Fore.RED + '-> [ E  S ] <-' + Style.RESET_ALL)
    if location.location == 'Storage Room':
        print(Fore.RED + '-> [ N  S  W ] <-' + Style.RESET_ALL)
    if location.location == 'Lavatory':
        print(Fore.RED + '-> [ E ] <-' + Style.RESET_ALL)
    if location.location == 'Grand Library':
        print(Fore.RED + '-> [ N  E ] <-' + Style.RESET_ALL)


currentPlayer = Player('Johnny', room['outside'], [])
location = currentPlayer.location
locationItems = []

print('\n\n')
print(Fore.BLUE + '====================================\n' + Style.RESET_ALL)
print('|          ' + Fore.RED + 'Pointless  Quest' +
      Style.RESET_ALL + '        |\n')
print('|        ' + Fore.YELLOW + '--------------------' +
      Style.RESET_ALL + '      |\n')
print('|              Q to quit           |\n')
print(Fore.BLUE + '====================================\n' + Style.RESET_ALL)

print('Enter your name to begin this Quest')
currentPlayer.name = input('Your Name -> ')
print(f"\n\n{currentPlayer.name}'s adventure begins!\n\n")

while True:
    print(Fore.BLUE + f'{location.location}\n' +
          Style.RESET_ALL + f'{location.description}')
    for item in location.items:
        locationItems.append(item.name)
    print(Fore.GREEN + f'{locationItems}' + Style.RESET_ALL)
    available_directions()
    cmd = input('\nEnter command -> ')
    player_movement(cmd)
    if cmd == 'q' or cmd == 'Q':
        print(Fore.YELLOW + '\nGoodbye!' + Style.RESET_ALL)
        break
