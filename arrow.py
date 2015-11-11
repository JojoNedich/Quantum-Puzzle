from colorama import *
import random

color_dict = {'white': Fore.WHITE, 'red': Fore.RED, 'blue': Fore.BLUE}
esc = Style.RESET_ALL


class Arrow(object):

    def __init__(self, color='white', is_up=False):
        self.is_up = is_up
        self.color = color_dict[color]

    def draw(self):
        if self.is_up:
            print (self.color + ' /\\ ' + esc, end=''),
        if not self.is_up:
            print (self.color + ' \\/ ' + esc, end=''),

    def flip(self):
        self.is_up = not self.is_up


#  methods for functionality
def red_flip(arrows):
    for arrow in arrows:
        if arrow.color == color_dict['red']:
            arrow.flip()


def print_arrow_list(arrows):
    for arrow in arrows:
        arrow.draw()
    print('')
    for i in range(1, len(arrows) + 1):
        print (' ' + arrows[i-1].color + str(i) + esc + '  ', end=''),
    print('')


def blue_flip(arrows, arrow):
    arrow.flip()
# in case the arrow you want to flip is at either end of the list
    try:
        arrows[(arrows.index(arrow)) - 1].flip()
    except:
        pass
    try:
        arrows[(arrows.index(arrow)) + 1].flip()
    except:
        pass


#generates a random list (solved)
def generate_rand_list(length):
    rand_color = {0: 'white', 1: 'red', 2: 'blue'}
    return [Arrow((rand_color[random.randrange(3)]), True) for i in range(length)]


#flips arrow according to color
def colored_flip(arrows, arrow):
    if arrow.color == color_dict['red']:
        red_flip(arrows)
        return
    if arrow.color == color_dict['blue']:
        blue_flip(arrows, arrow)
        return
    if arrow.color == color_dict['white']:
        arrow.flip()
        return


#makes an ordered list, disorders it and returns it
def generate_disordered_list(length):
    ordered_list = generate_rand_list(length)
    return shuffle_list(ordered_list)


# disorders the list by flipping according to color, insuring that the puzzle
# is solvable
def shuffle_list(arrows):
    ordered_list = arrows
    for i in range(20):
        colored_flip(ordered_list, ordered_list[
                     random.randrange(0, len(arrows))])

    return ordered_list
