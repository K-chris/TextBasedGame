# christopher Kooyman
# IT-140-H7429
# 22EW5
# 6/13/2022


def player_instructions():  # funct to print the game commands and objective
    print("Shipwrecked:A Space Game",
          "collect all 9 items and regain control of the ship, or die trying\n",
          "Move commands: GO NORTH,MOVE SOUTH, GO EAST, MOVE WEST\n",
          "Add item to Inventory: GET 'Item Name'\n",
          "Exit the game: EXIT\n\n")


def move_player(usr_choice, cur_room):  # function move player when user_choice contains MOVE or GO
    # checks to see what direction was inputted and compares it with room list to see if it's a valid move
    if usr_choice[1] in rooms.get(cur_room):
        return rooms[cur_room].get(usr_choice[1])  # updates room to new room and returns to main loop

    else:  # function prints that it's an invalid move and returns the same room back
        print("There is no door that way")
        return cur_room  # return current room back to main loop


def get_item(usr_choice, cur_room):  # function for getting items and putting into inventory
    if usr_choice[1] in items.get(cur_room).upper() and usr_choice[1] != 'NONE':  # checks to see if user input is
        # the same item in the current room
        inventory.append(items[cur_room])  # add item to inventory
        print("You obtained a {}".format(items[cur_room]))  # let user know they obtained an item
        items[cur_room] = 'NONE'  # set the item in the room to none so the user cannot pick it up again
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


def print_player_info(name):  # function for printing player info   #TODO CONSOLIDATE  INTO SH OW STATUS FUNCTION
    print("{}".format(name))  # Print users name
    print("Inventory :{}".format(inventory))  # print users current inventory


def print_room_info(cur_room):   #TODO CONSOLIDATE INTO SHOW STATUS FUNCTION
    print("you are currently in the: {}".format(cur_room))
    if items[cur_room] != 'NONE':
        print('You see a {} on the ground'.format(items[cur_room]))


def final_boss():
    print("You enter in the Cockpit ready for what horrors might be inside.")
    if len(inventory) == 9:

        print("the space pirate was unaware of your presence as you entered and you strike \n",
              "while he is unaware, taking him out with a single blast of your Phaser\n",
              'GAME OVER, YOU WIN!! Thanks for Playing')
    else:
        print("The space pirate was expecting you and had a ambush set up as you entered,/n",
              'blasting you to pieces.\n', 'GAME OVER, YOU LOSE. Thanks for Playing')


def main():
    player_name = None
    current_room = 'Lower Engines'  # TODO CHANGE TO Hanger Bay when deploying game
    player_instructions()
    while player_name is None:
        player_name = input('Enter in your player name: ')
        print('\n\n')

    while current_room != 'Cockpit':
        print_player_info(player_name)
        print_room_info(current_room)
        print('_________________________________________')
        user_choice = user_input()
        if user_choice[0] in ['GO', 'MOVE']:
            current_room = move_player(user_choice, current_room)
        elif user_choice[0] in 'GET':
            get_item(user_choice, current_room)
        elif user_choice[0] in 'EXIT':
            print("You decide to exit the abandoned ship, leaving behind the mystery of what had happened")
            print("Game Over, hope you had fun")
            return

    if current_room in 'Cockpit':
        final_boss()


if __name__ == '__main__':
    inventory = []
    commands = ['GET', 'MOVE', 'GO']

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
