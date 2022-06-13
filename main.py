import socket


def move_player(usr_choice, cur_room):  # function move player when user_choice contains MOVE or GO
    # checks to see what direction was inputted and compares it with room list to see if it's a valid move
    if usr_choice[1] in rooms.get(cur_room):
        return rooms[cur_room].get(usr_choice[1])  # updates room to new room and returns to main loop

    else:  # function prints that it's an invalid move and returns the same room back
        print("There is no door that way")
        return cur_room  # return current room back to main loop


def get_item(usr_choice, cur_room):  # function for getting items and putting into inventory
    if usr_choice[1] in items.get(cur_room).upper() and usr_choice[1] != 'NONE':  #checks to see if user input is the same item in the current room
        inventory.append(items[cur_room])  #add item to inventory
        print("You obtained a {}".format(items[cur_room]))  #let user know they obtained a item
        items[cur_room] = 'NONE'  #set the item in the room to none so the user cannot pick it up again
    else:
        print("Unable to obtain {}".format(usr_choice[1]))


def user_input():  # function user_input for processing user input and checkin if it's a valid command
    while True:  # loop while user input is invalid
        usr_choice = input('what would you like to do: ').upper()  # prompt user for input
        separated_input = usr_choice.split()  # separate the list by spaces
        if separated_input[0] in commands and len(
                separated_input) > 1:  # check to ensure input is valid and longer then 2
            separated_input[1:] = [' '.join(separated_input[1:])]  # combine user input back from 1 to end of list
            return separated_input  # returns the user input list of size 2


def print_player_info(name):  # function for printing player info
    print("{}".format(name))  # Print users name
    print("Inventory :{}".format(inventory))  # print users current inventory


def print_room_info(cur_room):
    print("you are currently in the: {}".format(cur_room))
    if items[cur_room] != 'NONE':
        print('You see a {} on the ground'.format(items[cur_room]))


def main():
    player_name = socket.gethostname()  # TODO CHANGE TO None when done testing
    current_room = 'Lower Engines'  # TODO CHANGE TO Hanger Bay when deploying game
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
        if user_choice[0] in ['GO', 'MOVE']:
            current_room = move_player(user_choice, current_room)
        elif user_choice[0] in 'GET':
            get_item(user_choice, current_room)
        # elif user_choice[0] ==


if __name__ == '__main__':
    inventory = []
    commands = ['GET', 'USE', 'MOVE', 'GO']
    door_locks = {  # DICTIONARY OF ROOM LOCK STATE
        'Cargo Bay': 'UNLOCKED',
        'Hanger Bay': 'UNLOCKED',
        'Lower Engines': 'UNLOCKED',
        'Generator Room': 'UNLOCKED',
        'Upper Engines': 'UNLOCKED',
        'Medical bay': 'LOCKED',
        'Crew Quarters': 'LOCKED',
        'Hallway': 'UNLOCKED',
        'Mess Hall': 'UNLOCKED',
        'Kitchen': 'UNLOCKED',
        'Cockpit': 'LOCKED'
    }
    items = {  # make a Dictionary of all rooms and what item might be in there
        'Cargo Bay': 'Corrupted Data Drive',
        'Hanger Bay': 'NONE',
        'Lower Engines': 'Fire Extinguisher',
        'Generator Room': 'Portable Shield Generator',
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
    main()
