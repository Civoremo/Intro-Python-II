from room import Room
from player import Player
from item import Item
from treasure import Treasure
from weapon import Weapon
from monster import Monster
from colorama import init, Fore, Back, Style
init(convert=True)

# Declare all available items
# name,description
# Weapon: name,description,attack_points
# Treasure: name,description,value=0

item = {
    'lamp': Item('Lamp', 'An old forgoten lamp with some oil still remaining.'),
    'pouch': Item('Pouch', 'Old, slightly torn pouch, usefull for carrying things.'),
    'sword': Weapon('Sword', 'Dull sword; good for smashing things.', 3),
    'coins': Treasure('Coins', 'Unfamiliar coins, might still hold some value.', 20),
    'artibact': Treasure('ArtiBact', 'Blue in color. Looks to be a piece of a bigger puzzle.', 35),
    'artiract': Treasure('ArtiRact', 'Red in color. Looks to be a piece of a bigger puzzle.', 35),
    'artiwact': Treasure('ArtiWact', 'White in color. Looks to be a piece of a bigger puzzle.', 35),
    'shield': Item(
        'Shield', 'Rotting piece of wood that may have been used as a shield in the past.'),
    'bow': Weapon('Bow', 'Magnificently crafted bow; missing string to be functional!', 1),
    'arrows': Weapon('Arrows', 'Deadly, pointy sticks.', 1),
    'jar': Item('Jar', 'Empty jar; can hold things.'),
    'flower': Item('Flower', 'A flower that grew out of stone.'),
    'mirror': Treasure('Mirror', 'Antique mirror, looks valuable.', 50),
    'chalise': Treasure('Chalise', 'A fancy cup to drink out of.', 120),
    'crown': Treasure('Crown', 'Long lost crown of ...', 200),
    'ruby': Treasure('Ruby', 'Precious stone; red I believe.', 75),
    'emerald': Treasure('Emerald', 'Precious stone; green I think.', 70),
    'pebbles': Item('Pebbles', 'No ordinary rocks, smooth edges.'),
    'slingshot': Weapon('Slingshot', "Dennis the Menace's favorite weapon.", 2),
    'slime': Item('Slime', 'Mysterious smelling goo.'),
    'dagger': Weapon('Dagger', 'A fancy knife used for tabbing.', 2),
    'hammer': Weapon('Hammer', 'A hammer Thor would be proud to have.', 4),
    'virus': Weapon('Virus', 'Highly infectious Zombie virus.', 2),
    'femur': Weapon('Femur', 'A bone club.', 3),
    'laser': Weapon('Laser', 'High intensity laser, can cause burns.', 3),
    'banana': Weapon('Banana', 'Slippery banana peel.', 2)
}

# Declare all the monsters
# name, weapon, health=5

monster = {
    'goblin': Monster('Goblin', item['dagger'], 10),
    'ogre': Monster('Ogre', item['hammer'], 18),
    'skeleton': Monster('Skeleton', item['femur'], 12),
    'zombie': Monster('Zombie', item['virus'], 10),
    'minion': Monster('Minion', item['banana'], 8),
    'boss': Monster('Boss', item['laser'], 25)
}



# Declare all the rooms
# Location,description,items,monsters,is_light

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.", [], [monster['boss']], True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north, east and west.""", [item['lamp']], [], True),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [item['flower'], item['artibact']], [], True),

    'narrow':   Room("Narrow Passage", """A narrow passage, the smell of gold permeates the air.""", [item['slime']], [], False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers.""", [item['artiwact'], item['pouch']], [monster['minion']], False),

    'chamber': Room('Bed Chamber', """A finely furnished bed chamber, all the things
are covered in dust and cob webs from years of neglect""", [item['mirror']], [], True),

    'cliff': Room('Cliff Edge', """Careful now, one small slip up and this could be the
end of your adventure.""", [item['flower']], [], True),

    'basement': Room('Pungent Basement', """Dark, cold, damp basement; gives me the creeps""", [item['sword']], [], False),

    'dungeon': Room('Dungeon', """Torture devices are scattered throughout the room""", [item['artiract']], [], False),

    'armory': Room('Armory', """A large room that used to hold a stockpile of weapons
but now it sits mostly empty""", [item['bow'], item['arrows']], [monster['ogre']], False),

    'cellar': Room('Wine Cellar', 'All the bottles are smashed. What a shame.', [item['shield']], [monster['skeleton']], False),

    'tunnel': Room('Long Corridor', 'Dark and narrow corridor, hard to see where it leads.', [item['slingshot']], [], False),

    'fountain': Room('Fountain of Youth', 'Elegantly decorated fountain; ice cold water still gushing.', [item['emerald'], item['ruby']], [monster['boss']], True),

    'alchemy': Room('Alchemy Chamber', """Elaborate contraptions scattered throughout the room
accompanied by an unbearable stench.""", [item['jar'], item['coins']], [monster['zombie']], False),

    'stairway': Room('Winding Stairway', """Caution, uneven steps!""", [item['pebbles']], [], False),

    'storage': Room('Storage Room', """Piles of junk knocked down on the floor""", [], [], False),

    'lavatory': Room('Lavatory', """Ocupado! sign tossed on the floor; doesn't
look like it was cleaned any time recently""", [item['crown']], [], True),

    'library': Room('Grand Library', 'Windows appear to be painted dark as to stop light from coming in', [item['chalise']], [monster['goblin']], False),

    'vendor': Room('Vendor', 'A place to sell valuables and make some schmekels.', [], [], True),
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
room['outside'].e_to = room['vendor']
room['vendor'].w_to = room['outside']


# instantiate player
currentPlayer = Player('', room['outside'], [item['sword']])

# player methods
def playerCommands(cmd):
    currentPlayer.travel(cmd)
    currentPlayer.action_help(cmd)
    currentPlayer.action_take(cmd)
    currentPlayer.action_drop(cmd)
    currentPlayer.action_use(cmd)
    currentPlayer.action_look(cmd)
    currentPlayer.attack(cmd)


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
              f'-> [ {currentPlayer.location.available_exits()} ] <-\n' + Style.RESET_ALL)
        if len(currentPlayer.location.monsters) > 0:
            print(Back.RED + Fore.BLACK + f" {currentPlayer.location.monsters} " + Style.RESET_ALL)
        else:
            print(f'')
    else:
        print(Fore.YELLOW + "It's pitch black!\n" + Style.RESET_ALL)
    cmd = input('\nEnter command -> ')
    playerCommands(cmd)
    if cmd.lower() == 'q':
        print(Fore.YELLOW +
              f'\nGoodbye {currentPlayer.name}' + Style.RESET_ALL)
        break
    if currentPlayer.schmekels > 450:
        print(Fore.GREEN +
              "You have earned enough schmekles; time to retire!\n" + Style.RESET_ALL)
        print(Fore.GREEN + "Try 'Pointless Quest' again.\n" + Style.RESET_ALL)
        break
