# christopher Kooyman
# IT-140-H7429
# 22EW5
# 6/13/2022


def player_instructions():  # function to print the game commands and objective
    print("Shipwrecked:A Space Game",
          "collect all 9 items and regain control of the ship, or die trying\n",
          "Move commands: GO NORTH,MOVE SOUTH, GO EAST, MOVE WEST\n",
          "Add item to Inventory: GET 'Item Name'\n",
          "Exit the game: EXIT\n\n\n\n\n\n\n\n",
          '_________________________________________')


def show_status(cur_room, rooms, inventory):  # function for printing player info and room info
    print("Inventory :{}\n".format(inventory),
          "you are currently in the: {}".format(cur_room))
    if rooms[cur_room]['ITEM'] != 'NONE':  # checks to see if item in the current room is not nothing
        print(' You see a {} on the ground'.format(rooms[cur_room]['ITEM']))  # prints item on floor if there is one
    print('_________________________________________')


def user_input():  # function user_input for processing user input and checkin if it's a valid command
    commands = ['GET', 'MOVE', 'GO']
    invalid_attempts = 0  # counter for failed input attempts
    while True:  # loop while user input is invalid
        usr_choice = input(' what would you like to do: ').upper()  # prompt user for input
        separated_input = usr_choice.split()  # separate the list by spaces
        # check to ensure input is valid and longer then 2
        if separated_input[0] in commands and len(separated_input) > 1:
            separated_input[1:] = [' '.join(separated_input[1:])]  # combine user input back from 1 to end of list
            print('\n' * 15,
                  '_________________________________________')
            return separated_input  # returns the user input list of size 2
        print(" sorry '{}' is not a valid command".format(separated_input[0]))
        invalid_attempts += 1  # increments invalid attempt by 1
        if invalid_attempts > 2:  # prints command list upon 3 successive invalid input attempts
            print('_________________________________________\n',
                  ' Remember the valid commands are\n',
                  "Move commands: GO NORTH,MOVE SOUTH, GO EAST, MOVE WEST\n",
                  "Add item to Inventory: GET 'Item Name'\n",
                  "Exit the game: EXIT\n",
                  '_________________________________________\n')


def move_player(usr_choice, cur_room, rooms):  # function move player when user_choice contains MOVE or GO
    # checks to see what direction was inputted and compares it with room list to see if it's a valid move
    if usr_choice[1] in rooms.get(cur_room):
        return rooms[cur_room].get(usr_choice[1])  # updates room to new room and returns to main loop

    else:  # function prints that it's an invalid move and returns the same room back
        print("There is no door that way")
        return cur_room  # return current room back to main loop


def get_item(usr_choice, cur_room, rooms, inventory):  # function for getting items and putting into inventory
    if usr_choice[1] in rooms[cur_room]['ITEM'].upper() and usr_choice[1] != 'NONE':  # checks to see if user input is
        # the same item in the current room
        inventory.append(rooms[cur_room]['ITEM'])  # add item to inventory
        print("You obtained a {}".format(rooms[cur_room]['ITEM']))  # let user know they obtained an item
        rooms[cur_room]['ITEM'] = 'NONE'  # set the item in the room to none so the user cannot pick it up again
    else:
        print("Unable to obtain {}".format(usr_choice[1]))


def final_boss(inventory):  # function for final boss fight
    print(" You enter in the Cockpit ready for what horrors might be inside.")
    if len(inventory) == 9:  # if you collected all the items you win, else you lose

        print(" The space pirate was unaware of your presence as you entered and you strike \n",
              "while he is unaware, taking him out with a single blast of your Phaser\n",
              'GAME OVER, YOU WIN!! Thanks for Playing')
    else:
        print(" The space pirate was expecting you and had a ambush set up as you entered,\n",
              'blasting you to pieces.\n', 'GAME OVER, YOU LOSE. Thanks for Playing')


def main():  # Main Function
    inventory = []  # Ini inventory
    rooms = {  # set Dictionary room to list of all rooms and the valid adjacent rooms and item(if any) in room
        'Cargo Bay': {'NORTH': 'Crew Quarters', 'WEST': 'Hanger Bay', 'ITEM': 'Corrupted Data Drive'},
        'Hanger Bay': {'EAST': 'Cargo Bay', 'WEST': 'Lower Engines', 'ITEM': 'NONE'},
        'Lower Engines': {'NORTH': 'Generator Room', "EAST": 'Hanger Bay', 'ITEM': 'Fire Extinguisher'},
        'Generator Room': {'NORTH': 'Upper Engines', 'SOUTH': 'Lower Engines', 'ITEM': 'Portable Shield Generator'},
        'Upper Engines': {'EAST': 'Medical bay', 'SOUTH': 'Generator Room', 'ITEM': 'Wrench'},
        'Medical bay': {'EAST': 'Crew Quarters', 'WEST': 'Upper Engines', 'ITEM': 'First Aid Kit'},
        'Crew Quarters': {'EAST': 'Hallway', 'SOUTH': "Cargo Bay", 'WEST': 'Medical bay', 'ITEM': 'Phaser'},
        'Hallway': {'SOUTH': 'Mess Hall', 'WEST': 'Crew Quarters', 'ITEM': 'Med-bay Key card'},
        'Mess Hall': {'NORTH': 'Hallway', 'EAST': 'Cockpit', 'SOUTH': 'Kitchen', 'ITEM': 'Mystery Meat Paste'},
        'Kitchen': {'NORTH': 'Mess Hall', 'ITEM': 'Kitchen Knife'},
        'Cockpit': {'WEST': 'Mess Hall', 'ITEM': 'NONE'}
    }
    current_room = 'Hanger Bay'  # set current room to starting room
    player_instructions()  # Call funct to display player instructions

    while current_room != 'Cockpit':  # check to see if user is in the boss room else loop
        show_status(current_room, rooms, inventory)  # show player info and current room info
        user_choice = user_input()  # set user_choice by calling user_input funct
        if user_choice[0] in ['GO', 'MOVE']:  # check to see what move user chose
            current_room = move_player(user_choice, current_room, rooms)  # set current room to move_player funct
        elif user_choice[0] in 'GET':
            get_item(user_choice, current_room, rooms, inventory)  # calls funct to get item off floor
        elif user_choice[0] in 'EXIT':  # else quit
            print("You decide to exit the abandoned ship, leaving behind the mystery of what had happened")
            print("Game Over, hope you had fun")
            return

    if current_room in 'Cockpit':  # check to ensure current room is cockpit
        final_boss(inventory)  # calls final boss funct


if __name__ == '__main__':
    main()  # calls main function
