# Maurice Conner SNHU IT-140
# December 1st, 2020

# Anime Brawl

import time

print('\n')
print('^<>^^><^^<>^^><^^<>^^><^^<>^^><^^<>^^><^^<>^^><^^<>^^><^^<>^^><^^<>^^><^^<>^^><^^<>^^><^^<>^^><^^<>^^><^^<>^')
print('\n')
print('....You slowly start to wake up and realize you are not in your bed but on something harder...')
print('\n')
time.sleep(4)
print('You jump up and look around')
print('\n')
time.sleep(2)
print('You are standing in a cave and confusion sets in as you try to remember your last steps')
print('\n')
time.sleep(5)
print('You had just gotten off of work and upon arriving home you decided to download this game your friend'
      ' told you about')
print('\n')
time.sleep(6)
print('You remember seeing a lot of familiar characters come across the screen as you waited....')
print('\n')
time.sleep(2)
print('At some point you must have fallen asleep.')
print('\n')
time.sleep(2)
print('As you think about this, a crazy thought pops into your head....what if you were downloaded into the game?')
print('\n')
time.sleep(4)
print('As soon as you fully process this thought words pop up in your mind....')
print('\n')
time.sleep(2)
print("'Welcome to the game, you must clear all areas and gather the treasure within them to defeat the boss'")
print('\n')
print('---------------------------------------------------------------------------------------------------------------')

# create instructions menu

def show_instructions():
    # prints main menu and commands
    print('\n')
    print('!!!!!ANIME BRAWL!!!!!')
    print('\n')
    print('Collect all items needed to beat the boss or die trying...')
    print('\n')
    print('Move commands: South, North, East, West')
    print('\n')
    print("Pick up item: get 'item name'.")
    print('\n')
    print("You can exit the game by typing in 'exit'")
    print('\n')
    print("Open menu by entering in 'help'")

print(show_instructions())

print('---------------------------------------------------------------------------------------------------------------')

def ending_question():
    anime_list = ('Outlaw Star', 'Naruto', 'DragonBall Z', 'Afro Samurai', 'Iron Man', 'Metroid')
    check_list = []

    first_question = input('Can you guess the title or name of the game the items in the game belong to?: ')
    print(first_question)

    if first_question == 'yes':

        while len(check_list) != len(anime_list):

            second_question = input('Make your guess: ')

            if second_question == 'exit':
                input('Are you ready to quit guessing?: ')
                print('Here is the list...hope you had fun!', anime_list)
                exit()

            if second_question not in check_list:

                if second_question in anime_list:

                    check_list.append(second_question)
                    print('Good guess!!! That is right')
                    print('So far you have correctly guessed: ', check_list)

                else:
                    print('No that is incorrect try again!!!')
                    print('So far you have correctly guessed: ', check_list)

            else:
                print('You have already guessed that answer, try again...')
                print('So far you have correctly guessed: ', check_list)

            if len(check_list) == len(anime_list):
                print('Congratulations!!! You have correctly guessed all the answers!!')

    elif first_question == 'no':

        first_question_ending = input('Are you ready to quit guessing?: ')
        print(first_question_ending)

        if first_question_ending == 'yes':
            print('Hopefully next time you can stay a while and play')
            time.sleep(2)
            exit()

        elif first_question_ending == 'no':
            ending_question()

        else:
            print("Please use 'yes' or 'no' to respond.")

    else:
        print("Please use 'yes' or 'no' to respond.")





def main():

    game_rooms = {
        'Starting Cavern': {'North': 'Mirror Room', 'East': 'Ball Room',
                            'South': 'Spaceship Wreckage', 'West': 'Zero Gravity Room'},
        'Mirror Room': {'East': 'Multi-Maze Forest', 'South': 'Starting Cavern',
                        'West': 'Secret Room', 'item': 'Forbidden Scroll'},
        'Multi-Maze Forest': {'West': 'Mirror Room', 'item': 'Time Sword'},
        'Secret Room': {'East': 'Mirror Room', 'item': 'Senzu Bean'},
        'Ball Room': {'West': 'Starting Cavern', 'North': 'Boss Cavern', 'item': 'Iron Suit'},
        'Boss Cavern': {'South': 'Ball Room', 'item': 'Moro'},
        'Spaceship Wreckage': {'North': 'Starting Cavern', 'East': 'Rolling Plains', 'item': 'Castor Gun'},
        'Rolling Plains': {'West': 'Spaceship Wreckage', 'item': 'Number 1 Headband'},
        'Zero Gravity Room': {'East': 'Starting Cavern', 'South': 'Upside-Down Cavern', 'item': 'Gravity Boots'},
        'Upside-Down Cavern': {'North': 'Zero Gravity Room', 'item': 'Plasma Shield'}
    }

    current_room = 'Starting Cavern'

    current_inventory = []

    full_inventory = sorted(['Forbidden Scroll', 'Time Sword', 'Iron Suit',
                      'Castor Gun', 'Number 1 Headband', 'Gravity Boots', 'Plasma Shield', 'Senzu Bean'])

    while True:

        room_item = game_rooms[current_room].get('item', 'nothing')

        print('\nYou are in the: \n','---->',current_room, '<----')
        print('\n')
        print('As you walk in the', current_room, ', you see the room has', room_item)
        print('------------------------------------------')
        print('Inventory: ', current_inventory)
        print('------------------------------------------\n')
        direction_choice = input('Enter your move: ')

        if direction_choice == 'exit':

            current_room = 'exit'

            print('\n')
            print('You are now in the', current_room)
            print('\n')
            final_question = input('Are you sure you are ready to quit the game? '
                                   ' ,would you like to try a guessing game first?: ')
            print('\n')
            print(final_question)

            if final_question == 'yes':
                print(ending_question())

            elif final_question == 'no':
                print('Thank you for playing')
                exit()

            else:
                print("Please answer 'yes' or 'no'...")

        elif direction_choice == 'get ' + room_item:

            if 'item' in game_rooms[current_room]:
                room_item = game_rooms[current_room].pop('item')
                current_inventory.append(room_item)
            else:
                print('You have already grabbed that item, move on to the next room....')

        elif direction_choice == 'help':
            print('\n')
            print('HELP/HELP/HELP/HELP/HELP/HELP/HELP/HELP/HELP/HELP/HELP/HELP/HELP/HELP/HELP/HELP/HELP/HELP/HELP/')
            print(show_instructions())
            print('------------------------------------------------------------------------------------------------')
            print('\n')

        elif direction_choice not in game_rooms[current_room]:
            print('***************************************************************************************************')
            print('\n')
            print('Input does not match valid direction or command, please try again')
            print('\n')
            print("'If you are unsure of what to do please type in 'help'")
            print('***************************************************************************************************')

        elif game_rooms[current_room][direction_choice] == 'Boss Cavern':

            if direction_choice not in game_rooms[current_room]:
                print(
                    '***************************************************'
                    '************************************************')
                print('\n')
                print('Input does not match valid direction or command, please try again')
                print('\n')
                print("'If you are unsure of what to do please type in 'help'")
                print(
                    '*************************************************'
                    '**************************************************')

            if sorted(current_inventory) == sorted(full_inventory):
                win_boss_question = input('You have gathered all items and stand ready to take the boss.'
                                          '.do you enter?: ')
                print(win_boss_question)

                if win_boss_question == 'yes':
                    print('You gear up and walk in and kill Moro.')
                    time.sleep(2)
                    print('Congratulations!!!! You have successfully completed the game!!!!')
                    time.sleep(3)
                    exit()

                elif win_boss_question == 'no':
                    continue

                else:
                    print("Please answer 'yes' or 'no'...")

            elif current_inventory != full_inventory:

                death_boss_question = input(
                    'Are you sure you you want to enter this room? You have not gathered all the required items: ')
                print(death_boss_question)

                if death_boss_question == 'yes':
                    print('You walk into the room and Moro destroys you and the world......')
                    print('\n')
                    print('Thank you for playing...You did not acquire all the necessary items')
                    print('Please play again and ensure to acquire all the items..')
                    print('\n')
                    print('The full item list is ...', full_inventory)
                    exit()

                elif death_boss_question == 'no':
                    continue

                else:
                    print("Please answer 'yes' or 'no'...")

    # elif for direction in current_room:
    #	if direction_choice in current_room

        elif direction_choice not in game_rooms[current_room]:
            print('***************************************************************************************************')
            print('\n')
            print('Input does not match valid direction or command, please try again')
            print('\n')
            print("'If you are unsure of what to do please type in 'help'")
            print('***************************************************************************************************')

        else:
            current_room = game_rooms[current_room][direction_choice]
            print('You are now in the', current_room)

print(main)

main()
