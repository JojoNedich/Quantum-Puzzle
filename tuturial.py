from arrow import *


def play_tuturial():
    print('==============')
    print('')
    print('Welcome to the tuturial.')
    print('Press \'Enter\' when you\'ve finnished with a lesson to move to the next one')
    print('Enter \'exit\' at any point to exit the tuturial')
    print('')
    print('==============')
    print('')

# break sequence:
    usr_in = input('')
    if usr_in == 'exit':
        return
    print('=========')

    example_white = [Arrow('white') for i in range(5)]
    print_arrow_list(example_white)
    print ('^ This is a row of arrows.')

    usr_in = input('')
    if usr_in == 'exit':
        return
    print('=========')

    print('')
    print('The goal of the game is to have all the arrows facing up')
    print('Like this:')
    example_solved = [Arrow('white', True) for i in range(5)]
    print_arrow_list(example_solved)

    usr_in = input('')
    if usr_in == 'exit':
        return
    print('=========')

    print('You do that by flipping them one at a time.')
    print('')
    print('You flip an arrow by entering the corresponding number')
    print('Example:')
    print('')
    print_arrow_list(example_white)
    print('')
    print('input: 2')
    example_white[1].flip()
    print_arrow_list(example_white)

    usr_in = input('')
    if usr_in == 'exit':
        return
    print('=========')

    print('Arrows have different properties according to their color.')
    ex_colored = generate_rand_list(7)
    print_arrow_list(ex_colored)

    usr_in = input('')
    if usr_in == 'exit':
        return
    print('=========')

    print('When flipping a red arrow, that will flip every other red arrow in the row:')
    red_ex = [Arrow('red') for i in range(7)]
    red_ex[1] = Arrow()
    red_ex[3] = Arrow()
    red_ex[5] = Arrow()
    print_arrow_list(red_ex)
    print('input: 3')
    red_flip(red_ex)
    print_arrow_list(red_ex)

    usr_in = input('')
    if usr_in == 'exit':
        return
    print('=========')

    print('Blue ones flip themselfs and the ones next to them')
    blue_ex = [Arrow() for i in range(7)]
    blue_ex[3] = Arrow('blue')
    print_arrow_list(blue_ex)
    print('Input 4:')
    colored_flip(blue_ex, blue_ex[3])
    print_arrow_list(blue_ex)

    usr_in = input('')
    if usr_in == 'exit':
        return
    print('=========')

    print('Simple enough?')
    print('Good.')
    print('Have fun')
