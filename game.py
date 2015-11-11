from arrow import *
import tuturial


def check_win_cond(arrows):
    for arrow in arrows:
        if not arrow.is_up:
            return False
    return True


def play_game():
    while True:
        try:
            user_input = int(input('Select size for puzzle: '))
            if user_input == 'exit':
                return
            user_input = int(user_input)
        except:
            print('Let\'s stick to numbers')
            continue
        if int(user_input > 10):
            print('Advised to keep it bellow 10')
        else:
            break

# making sure the list isn't solved already
    player_list = generate_disordered_list(user_input)
    while check_win_cond(player_list):
        player_list = generate_disordered_list(user_input)

    while True:
        print_arrow_list(player_list)
        try:
            user_input = (input('>'))
            if user_input == 'exit':
                return
            user_input = int(user_input)
        except:
            print('Let\'s stick to numbers')
            continue
        if user_input < 1 or user_input > len(player_list):
            print('That number is out of bounds')
        else:
            colored_flip(player_list, player_list[user_input - 1])
        if check_win_cond(player_list):
            print_arrow_list(player_list)
            exit_game()


#############################

def exit_game():
    print('Thanks for playing :)')
    quit()


print
print('--- Welcome to the Quantum Puzzle game ---')
print

while True:
    print('enter \'?\' for a quick tuturial on how to play the game')
    print('enter \'exit\' at any time to stop the aplication or come back to this menu')
    print('enter \'play\' to start the game')
    inp = input('>')
    if inp == 'exit':
        print
        exit_game()
        print
    elif inp == 'play':
        play_game()
    elif inp == '?':
        tuturial.play_tuturial()
