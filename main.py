def move_player(usr_choice, cur_room):  # function move player when user_choice contains MOVE or GO
    # checks to see what direction was inputted and compares it with room list to see if it's a valid move
    if usr_choice[1] in rooms.get(cur_room):

        return rooms[cur_room].get(usr_choice[1])  # updates room to new room
    else:  # function prints that it's an invalid move and returns the same room back
        print("There is no door that way")
        return cur_room


def get_item():
    return -1


def user_input():
    while True:
        usr_choice = input('what would you like to do: ').upper()
        separated_input = usr_choice.split()
        if separated_input[0] in commands:
            print(separated_input)
            return separated_input


def print_player_info(name):
    print("{}".format(name))
    print("Inventory :{}".format(inventory))


def print_room_info(cur_room):
    print("you are currently in the: {}".format(cur_room))
    if items[cur_room] != 'NONE':
        print('You see a {} on the ground'.format(items[cur_room]))


if __name__ == '__main__':
    player_name = 'CHAD'  # TODO CHANGE TO None when done testing
    current_room = 'Hanger Bay'
    inventory = []
    commands = ['GET', 'USE', 'MOVE', 'GO']
    items = {  # make a Dictionary of all rooms and what item might be in there
        'Cargo Bay': 'Corrupted Data Drive',
        'Hanger Bay': 'NONE',
        'Lower Engines': 'Fire Extinguisher',
        'Generator Room': 'Portable SHeld Generator',
        'Upper Engines': 'Wrench',
        'Medical bay': 'First Aid Kit',
        'Crew Quarters': 'Phaser',
        'Hallway': 'Med-bay Key card',
        'Mess Hall': 'Mystery Meat Paste',
        'Kitchen': 'Kitchen Knife',
        'Cockpit': 'NONE'
    }

    rooms = {  # set Dictionary room to list of all rooms and the valid adjacent rooms
        'Cargo Bay': {'NORTH': 'Crew Quarters', 'WEST': 'Hanger Bay'},
        'Hanger Bay': {'EAST': 'Cargo Bay', 'WEST': 'Lower Engines'},
        'Lower Engines': {'NORTH': 'Generator Room', "EAST": 'Hanger Bay'},
        'Generator Room': {'NORTH': 'Upper Engines', 'SOUTH': 'Lower Engines'},
        'Upper Engines': {'EAST': 'Medical bay', 'SOUTH': 'Generator Room'},
        'Medical bay': {'EAST': 'Crew Quarters', 'WEST': 'Upper Engines'},
        'Crew Quarters': {'EAST': 'Hallway', 'SOUTH': "Cargo Bay", 'WEST': 'Medical bay'},
        'Hallway': {'SOUTH': 'Mess Hall', 'WEST': 'Crew Quarters'},
        'Mess Hall': {'NORTH': 'Hallway', 'EAST': 'Cockpit', 'SOUTH': 'Kitchen'},
        'Kitchen': {'NORTH': 'Mess Hall'},
        'Cockpit': {'WEST': 'Mess Hall'}
    }

    print("Untitled:A Space Game")
    print("collect items and unlock the way to the boss to win")
    print("Move commands: GO NORTH,GO SOUTH, GO EAST GO WEST")
    print("Add item to Inventory: GET 'Item Name'")
    print("USE item from Inventory: USE 'Item Name'\n")

    while player_name is None:
        player_name = input('Enter in your player name: ')
        print('\n\n')

    while True:
        print_player_info(player_name)
        print_room_info(current_room)
        print('_________________________________________')

        user_choice = user_input()
        if user_choice[0] == 'MOVE' or 'GO':
            current_room = move_player(user_choice, current_room)
        # elif user_choice[0] ==
        # elif user_choice[0] ==
