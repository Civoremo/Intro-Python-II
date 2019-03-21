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
    'artibact': Item('ArtiBact', 'Blue in color. Looks to be a piece of a bigger puzzle.'),
    'artiract': Item('ArtiRact', 'Red in color. Looks to be a piece of a bigger puzzle.'),
    'artiwact': Item('ArtiWact', 'White in color. Looks to be a piece of a bigger puzzle.'),
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
                     "North of you, the cave mount beckons.", [], True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [item['lamp']], True),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [item['flower'], item['artibact']], True),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [item['slime']], False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [item['artiwact'], item['pouch']], False),

    'chamber': Room('Bed Chamber', """A finely furnished bed chamber, all the things
are covered in dust and cob webs from years of neglect""", [item['mirror']], True),

    'cliff': Room('Cliff Edge', """Careful now, one small slip up and this could be the
end of your adventure.""", [item['flower']], True),

    'basement': Room('Pungent Basement', """Dark, cold, damp basement; gives me the creeps""", [item['sword']], False),

    'dungeon': Room('Dungeon', """Torture devices are scattered throughout the room""", [item['artiract']], False),

    'armory': Room('Armory', """A large room that used to hold a stockpile of weapons
but now it sits mostly empty""", [item['bow'], item['arrows']], False),

    'cellar': Room('Wine Cellar', 'All the bottles are smashed. What a shame.', [item['shield']], False),

    'tunnel': Room('Long Corridor', 'Dark and narrow corridor, hard to see where it leads.', [item['slingshot']], False),

    'fountain': Room('Fountain of Youth', 'Elegantly decorated fountain; ice cold water still gushing.', [item['emerald'], item['ruby']], True),

    'alchemy': Room('Alchemy Chamber', """Elaborate contraptions scattered throughout the room
accompanied by an unbearable stench.""", [item['jar'], item['coins']], False),

    'stairway': Room('Winding Stairway', """Caution, uneven steps!""", [item['pebbles']], False),

    'storage': Room('Storage Room', """Piles of junk knocked down on the floor""", [], False),

    'lavatory': Room('Lavatory', """Ocupado! sign tossed on the floor; doesn't
look like it was cleaned any time recently""", [item['crown']], True),

    'library': Room('Grand Library', 'Windows appear to be painted dark as to stop light from coming in', [item['chalise']], False),
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


# instantiate player
currentPlayer = Player('', room['outside'], [])


def playerCommands(cmd):
    currentPlayer.travel(cmd)
    currentPlayer.action_help(cmd)
    currentPlayer.action_take(cmd)
    currentPlayer.action_drop(cmd)
    currentPlayer.action_use(cmd)


# Game Title Screen
print('\n\n')
print(Fore.BLUE + '====================================\n' + Style.RESET_ALL)
print('|          ' + Fore.RED + 'Pointless  Quest' +
      Style.RESET_ALL + '        |\n')
print('|        ' + Fore.YELLOW + '--------------------' +
      Style.RESET_ALL + '      |\n')
print('|              Q to quit           |\n')
print('|            Help for info         |\n')
print(Fore.BLUE + '====================================\n' + Style.RESET_ALL)

print('Enter your name to begin this Quest')
currentPlayer.name = input('Your Name -> ')
print(f"\n\n{currentPlayer.name}'s adventure begins!\n\n")


# Main Game Loop
while True:
    if currentPlayer.location.is_light == True:
        print(Fore.BLUE + f'{currentPlayer.location.location}\n' +
              Style.RESET_ALL + f'{currentPlayer.location.description}')
        print(Fore.GREEN + f'{currentPlayer.location.items}' + Style.RESET_ALL)
        print(Fore.MAGENTA +
              f'-> [ {currentPlayer.location.available_exits()} ] <-' + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + "It's pitch black!\n" + Style.RESET_ALL)
    cmd = input('\nEnter command -> ')
    playerCommands(cmd)
    if cmd.lower() == 'q':
        print(Fore.YELLOW +
              f'\nGoodbye {currentPlayer.name}' + Style.RESET_ALL)
        break
