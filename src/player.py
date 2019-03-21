# Write a class to hold player information, e.g. what room they are in
# currently.
from colorama import init, Fore, Back, Style
init(convert=True)


class Player:
    def __init__(self, name, location, items):
        self.name = name
        self.location = location
        self.items = items

    def __str__(self):
        return f'Your location: "{self.location}"'

    def __repr__(self):
        return f"Your location: '{self.location}'"

    def addItemToUser(self, item):
        self.items.append(item)

    def removeItemFromUser(self, item):
        for index, i in enumerate(self.items):
            if i == item:
                self.items.pop(index)

    def travel(self, direction):
        if len(direction.split(' ')) == 1:
            if direction in ["n", 'e', 's', 'w']:
                next_room = self.location.get_new_location(direction)
                if next_room is not None:
                    self.location = next_room
                    if direction == 'n':
                        print(Fore.YELLOW + '\n\n_-_-_-' +
                              Style.RESET_ALL + ' Walked North\n')
                    elif direction == 'e':
                        print(Fore.YELLOW + '\n\n_-_-_-' +
                              Style.RESET_ALL + ' Walked East\n\n')
                    elif direction == 's':
                        print(Fore.YELLOW + '\n\n_-_-_-' +
                              Style.RESET_ALL + ' Walked South\n\n')
                    elif direction == 'w':
                        print(Fore.YELLOW + '\n\n_-_-_-' +
                              Style.RESET_ALL + ' Walked West\n\n')
                    else:
                        print(Fore.YELLOW + '\n\n_-_-_-' +
                              Style.RESET_ALL + ' Wondering around\n\n')
                else:
                    print("\n\nCan't go in that direction\n")
        else:
            return None

    def action_help(self, action):
        if len(action.split(' ')) == 1:
            if action.lower() == 'i':
                inventory = []
                print(Fore.CYAN +
                      f"\n{self.name}'s Inventory" + Style.RESET_ALL)
                for i in self.items:
                    inventory.append(i)
                print(f'{inventory}\n')
            elif action.lower() == 'help':
                print('\nKeywords')
                print(Back.BLUE + ' take ' + Style.RESET_ALL +
                      ' -> Used with "item_name" to pick up item')
                print(Back.BLUE + ' drop ' + Style.RESET_ALL +
                      '-> Used with "item_name" to drop item')
                print(Back.BLUE + ' use ' + Style.RESET_ALL +
                      '-> Used with "item_name" to use item in inventory')
                print(Back.BLUE + ' look ' + Style.RESET_ALL +
                      '-> Used to inspect items in your inventory')
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
                return None

    def action_take(self, action):
        commands = action.split(" ")
        if len(action.split(' ')) == 2:
            if commands[0] == 'take':
                if self.location.is_light == True:
                    for i in self.location.items:
                        if commands[1].lower() == i.name.lower():
                            self.addItemToUser(i)
                            self.location.removeItemFromRoom(i)
                            print(Fore.YELLOW +
                                  f'\nYou picked up {i}\n' + Style.RESET_ALL)
                            break
                    else:
                        print(Fore.RED + '\nItem not found\n' + Style.RESET_ALL)
                else:
                    print(Fore.YELLOW +
                          "\nGood luck finding that in the dark!" + Style.RESET_ALL)
        else:
            return None

    def action_drop(self, action):
        commands = action.split(" ")
        if len(action.split(' ')) == 2:
            if commands[0] == 'drop':
                cmd = 'n'
                for i in self.items:
                    if commands[1].lower() == i.name.lower():
                        if i.name.lower() == 'lamp':
                            print(
                                Fore.YELLOW + "\nIt's not wise to drop your source of light!" + Style.RESET_ALL)
                            cmd = input('Still want to drop it [y,n]? -> ')
                        if i.name.lower() != 'lamp' or cmd.lower() == 'y':
                            self.removeItemFromUser(i)
                            self.location.addItemToRoom(i)
                            print(Fore.YELLOW +
                                  f'\nYou dropped {i}\n' + Style.RESET_ALL)
                            break
                        elif cmd.lower() == 'n':
                            print(Fore.YELLOW +
                                  f'\nYou kept the {i}\n' + Style.RESET_ALL)
                            cmd = 'n'
                            break
                else:
                    print(Fore.RED + '\nItem not found\n' + Style.RESET_ALL)
        else:
            return None

    def action_use(self, action):
        commands = action.split(" ")
        if len(action.split(' ')) == 2:
            if commands[0] == 'use':  # use command
                for i in self.items:
                    if commands[1].lower() == i.name.lower():
                        if self.location.is_light == False and i.name.lower() == 'lamp':
                            self.location.is_light = True
                            print(
                                Fore.YELLOW + '\nThe lamp illuminates the entire room and you can finally see.\n' + Style.RESET_ALL)
                            break
                        if self.location.is_light == True and i.name.lower() == 'lamp':
                            print(
                                Fore.YELLOW + "\nThis won't do anything, it's already bright in here.\n" + Style.RESET_ALL)
                            break
                        if i.name.lower() == 'pouch':
                            print(
                                Fore.YELLOW + '\nThere is nothing inside the pouch.\n' + Style.RESET_ALL)
                            break
                        if i.name.lower() == 'sword':
                            print(
                                Fore.YELLOW + '\nYou swing the sword at nothing and only got yourself tired.\n' + Style.RESET_ALL)
                            break
                        if i.name.lower() == 'coins':
                            print(
                                Fore.YELLOW + "\nYou can't do anything with the coins here.\n" + Style.RESET_ALL)
                            break
                        if i.name.lower() == 'artibact' or i.name.lower() == 'artiract' or i.name.lower() == 'artiwact':
                            print(
                                Fore.YELLOW + f"\nYou can't do anything with {i.name} here\n" + Style.RESET_ALL)
                            break
                        if i.name.lower() == 'shield':
                            print(
                                Fore.YELLOW + "\nShield slips out of your hands and falls on your toes.\n" + Style.RESET_ALL)
                            break
                        if i.name.lower() == 'bow':
                            print(
                                Fore.YELLOW + "\nCan't do anything with it; Bow is not functional\n" + Style.RESET_ALL)
                            break
                        if i.name.lower() == 'arrows':
                            print(
                                Fore.YELLOW + "\nYou throw the arrow against the wall and it breaks making it useless.\n" + Style.RESET_ALL)
                            break
                        if i.name.lower() == 'jar':
                            print(
                                Fore.YELLOW + "\nYou take a sip from it but it's empty.\n" + Style.RESET_ALL)
                            break
                        if i.name.lower() == 'flower':
                            print(
                                Fore.YELLOW + "\nSmelling the flower reminds you of back home.\n" + Style.RESET_ALL)
                            break
                        if i.name.lower() == 'mirror':
                            print(
                                Fore.YELLOW + "\nYou admire yourself in the mirror as you walk into a wall.\n" + Style.RESET_ALL)
                            break
                        if i.name.lower() == 'chalise':
                            print(
                                Fore.YELLOW + "\nYou raise the Chalise into the air and pretend to give a toast.\n" + Style.RESET_ALL)
                            break
                        if i.name.lower() == 'crown':
                            print(
                                Fore.YELLOW + "\nYou put the crown on your head and immediately start to feel like a million schmeckles.\n" + Style.RESET_ALL)
                            break
                        if i.name.lower() == 'ruby':
                            print(
                                Fore.YELLOW + "\nYou look through it and the surrounding turns red.\n" + Style.RESET_ALL)
                            break
                        if i.name.lower() == 'emerald':
                            print(
                                Fore.YELLOW + "\nYou look through it and the surrounding turns green.\n" + Style.RESET_ALL)
                            break
                        if i.name.lower() == 'pebbles':
                            print(
                                Fore.YELLOW + "\nYou throw one of the pebbles and a loud clank is heard as it hit a wall.\n" + Style.RESET_ALL)
                            break
                        if i.name.lower() == 'slingshot':
                            print(
                                Fore.YELLOW + "\nYou hear a faint voice yelling 'Deeeeennnnniiiiisssss.'\n" + Style.RESET_ALL)
                            break
                        if i.name.lower() == 'slime':
                            print(
                                Fore.YELLOW + "\nYou take a taste and immediately regret that decision.\n" + Style.RESET_ALL)
                            break
                        else:
                            return None
                else:
                    print(Fore.RED + "\nYou don't have that item.\n" +
                          Style.RESET_ALL)
            else:
                return None
        else:
            return None

    def action_look(self, action):
        commands = action.split(" ")
        if len(action.split(' ')) == 2:
            if commands[0] == 'look':
                for i in self.items:
                    if commands[1].lower() == i.name.lower():
                        print(Fore.YELLOW +
                              f'\n{i.description}\n' + Style.RESET_ALL)
                        break
                else:
                    print(Fore.RED + '\nItem not found\n' + Style.RESET_ALL)
        else:
            return None
