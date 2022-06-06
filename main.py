

def move_player():
    return -1

def get_item():
    return -1


def user_input(commands):
    while True:
        user_choice=input('what would you like to do: ').upper()
        seperated_input=user_choice.split()
        if seperated_input[0] in commands:
            print(seperated_input)
            return seperated_input


def print_player_info(name,inventory):
    print("{}".format(name))
    print("Inventory :[]".format(inventory))

def print_room_info(current_room,items):
    print("you are currently in the: {}".format(current_room))
    if(items[current_room]!='NONE'):
        print('You see a {} on the ground'.format(items[current_room]))

if __name__ == '__main__':
    player_name=None
    current_room='Hanger Bay'
    inventory=[]
    commands=['GET','USE','MOVE','GO']
    items={
        'Cargo Bay': 'Corrupted Data Drive',
        'Hanger Bay': 'NONE',
        'Lower Engines': 'Fire Extinguisher',
        'Generator Room': 'Portable SHield Generator',
        'Upper Engines': 'Wrench',
        'Medical bay': 'First Aid Kit',
        'Crew Quarters': 'Phaser',
        'Hallway':'Medbay Key card',
        'Mess Hall': 'Mystery Meat Paste',
        'Kitchen': 'Kitchen Knife',
        'Cockpit': 'NONE'
    }

    rooms={
        'Cargo Bay': {'NORTH':'Crew Quarters', 'WEST': 'Hanger Bay'},
        'Hanger Bay': {'EAST':'Cargo Bay','WEST':'Lower Engine'},
        'Lower Engines': {'NORTH':'Generator Room',"EAST":'Hanger Bay'},
        'Generator Room': {'North':'Upper Engines','SOUTH':'Lower Engines'},
        'Upper Engines': {'EAST':'Medical bay','SOUTH':'Generator Room'},
        'Medical bay': {'EAST': 'Crew Quarters','WEST':'Upper Engines'},
        'Crew Quarters':{'EAST':'Hallway','SOUTH':"Cargo Bay"},
        'Hallway':{'SOUTH':'Mess Hall', 'WEST': 'Crew Quarters'},
        'Mess Hall':{'NORTH':'Hallway', 'EAST':'Cockpit','SOUTH':'Kitchen'},
        'Kitchen':{'North':'Mess Hall'},
        'Cockpit':{'WEST':'Mess Hall'}
    }

    print("Untitled:A Space Game")
    print("collect items and unlock the way to the boss to win")
    print("Move commands: GO NORTH,GO SOUTH, GO EAST GO WEST")
    print("Add item to Inventory: GET 'Item Name'")
    print("USE item from Inventory: USE 'Item Name'\n")
    x=1

    while player_name is None:
        player_name=input('Enter in your player name: ')
        print('\n\n')

    while True:
        print_player_info(player_name,inventory)
        print_room_info(current_room,items)
        print('_________________________________________')

        user_choice=user_input(commands)
        if user_choice[0]=='MOVE' or 'go'
            move_player
        #elif user_choice[0] ==
        #elif user_choice[0] ==

        break