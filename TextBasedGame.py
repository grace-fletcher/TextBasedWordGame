# Grace Fletcher


# Function to print out the player's status
def get_status(room, inv):
    print('****************************************')
    print('Current room: {}'.format(room))
    print('Inventory: {} keys'.format(inv.count('key')))
    print('****************************************')


# Function to print out the game's instructions.
def get_instructions():
    print('------------------------------------------------------------------------------------------')
    print('Welcome to The Wizard Tower Text-Based Game!')
    print('Move between rooms by typing "Go" followed by the direction you would like to move!')
    print('Valid directions: "North", "South", "East", "West"')
    print('To get an item from a room, type "get item".')
    print('To check your status at any point in the game, type "get status".')
    print('You can also access these instructions at any time by typing "get instructions"!')
    print('Win the game by collecting all 7 keys!')
    print('Watch out for the wizard! If you run into him, it is game over!')
    print('To exit this game, simply type "exit".')
    print('------------------------------------------------------------------------------------------')


# Defines the main function (contains gameplay processes).
def main():
    # A dictionary that links rooms to other rooms as well as the items within them.
    rooms = {
        'Dungeon Cell': {'South': 'Potion Room', 'item': 'key'},
        'Potion Room': {'North': 'Dungeon Cell', 'West': 'Living Room', 'item': 'key'},
        'Living Room': {'North': 'Kitchen', 'West': 'Wizard Room', 'South': 'Library', 'item': 'key'},
        'Wizard Room': {'East': 'Living Room', 'item': 'wizard'},
        'Kitchen': {'South': 'Living Room', 'East': 'Garden', 'item': 'key'},
        'Garden': {'West': 'Kitchen', 'item': 'key'},
        'Library': {'North': 'Living Room', 'East': 'Kennel', 'item': 'key'},
        'Kennel': {'West': 'Library', 'item': 'key'}
    }

    # This 'directions' list contains valid cardinal directions to be referenced later.
    directions = ['North', 'South', 'East', 'West']

    # Initializes an empty 'inventory' list.
    inventory = []

    # Starts the player off in the Great Hall.
    current_room = 'Dungeon Cell'

    # Displays the game's instructions as well as the player's current status before beginning game.
    get_instructions()
    get_status(current_room, inventory)

    # Boolean value that turns the game on or off.
    game_on = True

    # While loop that facilitates the processes of moving between rooms and getting items.
    while game_on:
        # If statement to determine if the player has found all items.
        if inventory.count('key') == 7:
            print("Congratulations! You have found all 7 keys and escaped the wizard's tower!")
            print('Thanks for playing!')
            game_on = False

        # Variable that stores the user's input.
        command = input('Please enter a command:\n').split()

        # *Nested if-else statements to move between rooms, get an item, or exit the game depending on the given
        # command.*

        # Nested if-else statement to move players between rooms or end the game if the 'Wizard Room' is entered.
        if command[-1] in directions:
            if command[-1] in rooms[current_room]:
                if rooms[current_room][command[-1]] == 'Wizard Room':
                    print('Oh no! The wizard found you!')
                    print('Game Over')
                    game_on = False
                else:
                    current_room = rooms[current_room][command[-1]]
                    get_status(current_room, inventory)
            # Else statement for when the player enters an invalid direction.
            else:
                print('You cannot go that way!')

        # Nested if-else statement to add items to the player's inventory
        elif command[-1] == 'item':
            if 'item' in rooms[current_room]:
                if rooms[current_room]['item'] == 'key':
                    inventory.append('key')
                    del rooms[current_room]['item']
                    print('Yay! You found a key!')
                    get_status(current_room, inventory)
            # Else statement for when the room contains no 'item'.
            else:
                print('This room contains nothing of value.')

        # Else-if statements to check for game instructions, status, or exit commands.
        elif command[-1] == 'instructions':
            get_instructions()
        elif command[-1] == 'status':
            get_status(current_room, inventory)
        elif 'exit' in command:
            print('Exiting game')
            game_on = False

        # Else statement for debugging purposes.
        else:
            print('Invalid command')


# Runs the main function.
main()
