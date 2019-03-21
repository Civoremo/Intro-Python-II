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


def player_movement(player_input):

    # if input only contains one work, we assume player wants to move
    if len(player_input.split(' ')) == 1:
        try:
            if player_input.lower() == 'n':
                currentPlayer.location = currentPlayer.location.n_to
                print(Fore.YELLOW + '\n\n_-_-_-' +
                      Style.RESET_ALL + ' Walked North\n')
            elif player_input.lower() == 's':
                currentPlayer.location = currentPlayer.location.s_to
                print(Fore.YELLOW + '\n\n_-_-_-' +
                      Style.RESET_ALL + ' Walked South\n\n')
            elif player_input.lower() == 'e':
                currentPlayer.location = currentPlayer.location.e_to
                print(Fore.YELLOW + '\n\n_-_-_-' +
                      Style.RESET_ALL + ' Walked East\n\n')
            elif player_input.lower() == 'w':
                currentPlayer.location = currentPlayer.location.w_to
                print(Fore.YELLOW + '\n\n_-_-_-' +
                      Style.RESET_ALL + ' Walked West\n\n')
            elif player_input.lower() == 'q':
                print('')
            elif player_input.lower() == 'i':
                inventory = []
                print(Fore.CYAN + '\nPlayer Inventory' + Style.RESET_ALL)
                for i in currentPlayer.items:
                    inventory.append(i)
                print(f'{inventory}\n')
            elif player_input.lower() == 'help':
                print('\nKeywords')
                print(Back.BLUE + ' take ' + Style.RESET_ALL +
                      ' -> Used with "item_name" to pick up item')
                print(Back.BLUE + ' drop ' + Style.RESET_ALL +
                      '-> Used with "item_name" to drop item')
                print(Back.BLUE + ' i ' + Style.RESET_ALL +
                      '-> Checks your inventory')
                print(Back.BLUE + ' N,E,S,W ' + Style.RESET_ALL +
                      '-> Cardinal directions to move player')
                print(Fore.BLUE + ' Text ' + Style.RESET_ALL +
                      '-> Name of current location')
                print(Fore.GREEN + ' [] ' + Style.RESET_ALL +
                      '-> Items visible in current location')
                print(Fore.MAGENTA + ' ->[]<- ' + Style.RESET_ALL +
                      '-> Directions you can move to from current location\n\n')
            else:
                print(
                    Fore.RED + '\n--- Not a valid command, Try Again! ---\n' + Style.RESET_ALL)
        except:
            print(
                Fore.RED + '\n--- Not a valid command, Try Again! ---\n' + Style.RESET_ALL)
    else:
        return None


def player_action(player_input):

    commands = player_input.split(" ")  # splits input into list

    # if input contains more than 1 work we assume that player wants to perform an action
    # more than 2 words will ask user to type command again
    # if first command is not "take" or "drop", user will be asked to type command again

    if len(player_input.split(' ')) > 1:

        if commands[0] == 'take':
            if currentPlayer.location.is_light == True:
                for i in currentPlayer.location.items:
                    if commands[1].lower() == i.name.lower():
                        currentPlayer.addItemToUser(i)
                        currentPlayer.location.removeItemFromRoom(i)
                        print(Fore.YELLOW +
                              f'\nYou picked up {i}\n' + Style.RESET_ALL)
                    break
                else:
                    print(Fore.RED + '\nItem not found\n' + Style.RESET_ALL)
            else:
                print(Fore.YELLOW +
                      "\nGood luck finding that in the dark!" + Style.RESET_ALL)
        elif commands[0] == 'drop':
            cmd = 'n'
            for i in currentPlayer.items:
                if commands[1].lower() == i.name.lower():
                    if i.name.lower() == 'lamp':
                        print(
                            Fore.YELLOW + "\nIt's not wise to drop your source of light!" + Style.RESET_ALL)
                        cmd = input('Still want to drop it? -> ')
                    if i.name.lower() != 'lamp' or cmd.lower() == 'y':
                        currentPlayer.removeItemFromUser(i)
                        currentPlayer.location.addItemToRoom(i)
                        print(Fore.YELLOW +
                              f'\nYou dropped {i}\n' + Style.RESET_ALL)
                    elif cmd.lower() == 'n':
                        print(Fore.YELLOW +
                              f'\nYou kept the {i}\n' + Style.RESET_ALL)
                        cmd = 'n'
                break
            else:
                print(Fore.RED + '\nItem not found\n' + Style.RESET_ALL)
        else:
            print(
                Fore.RED + '\n--- Not a valid command, Try Again! ---\n' + Style.RESET_ALL)
    else:
        return None


def available_directions():
    if currentPlayer.location.location == 'Outside Cave Entrance':
        print(Fore.MAGENTA + '-> [ N ] <-' + Style.RESET_ALL)
    if currentPlayer.location.location == 'Foyer':
        print(Fore.MAGENTA + '-> [ N  E  S  W ] <-' + Style.RESET_ALL)
    if currentPlayer.location.location == 'Grand Overlook':
        print(Fore.MAGENTA + '-> [ S ] <-' + Style.RESET_ALL)
    if currentPlayer.location.location == 'Narrow Passage':
        print(Fore.MAGENTA + '-> [ N  E  W ] <-' + Style.RESET_ALL)
    if currentPlayer.location.location == 'Treasure Chamber':
        print(Fore.MAGENTA + '-> [ N  S ] <-' + Style.RESET_ALL)
    if currentPlayer.location.location == 'Bed Chamber':
        print(Fore.MAGENTA + '-> [ W  S ] <-' + Style.RESET_ALL)
    if currentPlayer.location.location == 'Cliff Edge':
        print(Fore.MAGENTA + '-> [ N ] <-' + Style.RESET_ALL)
    if currentPlayer.location.location == 'Pungent Basement':
        print(Fore.MAGENTA + '-> [ N  E  S ] <-' + Style.RESET_ALL)
    if currentPlayer.location.location == 'Dungeon':
        print(Fore.MAGENTA + '-> [ W  S ] <-' + Style.RESET_ALL)
    if currentPlayer.location.location == 'Armory':
        print(Fore.MAGENTA + '-> [ N ] <-' + Style.RESET_ALL)
    if currentPlayer.location.location == 'Wine Cellar':
        print(Fore.MAGENTA + '-> [ W  S ] <-' + Style.RESET_ALL)
    if currentPlayer.location.location == 'Long Corridor':
        print(Fore.MAGENTA + '-> [ N  E  S  W ] <-' + Style.RESET_ALL)
    if currentPlayer.location.location == 'Fountain of Youth':
        print(Fore.MAGENTA + '-> [ S ] <-' + Style.RESET_ALL)
    if currentPlayer.location.location == 'Alchemy Chamber':
        print(Fore.MAGENTA + '-> [ N ] <-' + Style.RESET_ALL)
    if currentPlayer.location.location == 'Winding Stairway':
        print(Fore.MAGENTA + '-> [ E  S ] <-' + Style.RESET_ALL)
    if currentPlayer.location.location == 'Storage Room':
        print(Fore.MAGENTA + '-> [ N  S  W ] <-' + Style.RESET_ALL)
    if currentPlayer.location.location == 'Lavatory':
        print(Fore.MAGENTA + '-> [ E ] <-' + Style.RESET_ALL)
    if currentPlayer.location.location == 'Grand Library':
        print(Fore.MAGENTA + '-> [ N  E ] <-' + Style.RESET_ALL)


# instantiate player
currentPlayer = Player('', room['outside'], [])

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
    locationItems = []
    if currentPlayer.location.is_light == True:
        print(Fore.BLUE + f'{currentPlayer.location.location}\n' +
              Style.RESET_ALL + f'{currentPlayer.location.description}')
        print(Fore.GREEN + f'{currentPlayer.location.items}' + Style.RESET_ALL)
        available_directions()
    else:
        print(Fore.YELLOW + "It's pitch black!\n" + Style.RESET_ALL)
    cmd = input('\nEnter command -> ')
    player_movement(cmd)
    player_action(cmd)
    if cmd == 'q' or cmd == 'Q':
        print(Fore.YELLOW + '\nGoodbye!' + Style.RESET_ALL)
        break
