from colorama import *
import random

color_dict = {'white': Fore.WHITE, 'red': Fore.RED, 'blue': Fore.BLUE,
              'yellow': Fore.YELLOW}
esc = Style.RESET_ALL

color_order = [color_dict['white'], color_dict['red'], color_dict['blue'],
               color_dict['yellow']]


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


def yellow_flip(arrows, arrow):
# in case the arrow you want to flip is at either end of the list
    if (arrows.index(arrow) != 0):
        cycle_color(arrows[(arrows.index(arrow)) - 1])
    if (arrows.index(arrow) != len(arrows) - 1):
        cycle_color(arrows[(arrows.index(arrow)) + 1])


def cycle_color(arrow):
    if (arrow.color == color_dict['red']):
        arrow.color = color_dict['blue']
    elif (arrow.color == color_dict['blue']):
        arrow.color = color_dict['red']
    elif (arrow.color == color_dict['yellow']):
        arrow.color = color_dict['white']
    elif (arrow.color == color_dict['white']):
        arrow.color = color_dict['yellow']




def print_arrow_list(arrows):
    for arrow in arrows:
        arrow.draw()
    print('')
    for i in range(1, len(arrows) + 1):
        print (' ' + arrows[i - 1].color + str(i) + esc + '  ', end=''),
    print('')


def blue_flip(arrows, arrow):
    arrow.flip()
# in case the arrow you want to flip is at either end of the list
    if (arrows.index(arrow) != 0):
        arrows[(arrows.index(arrow)) - 1].flip()
    if (arrows.index(arrow) != len(arrows) - 1):
        arrows[(arrows.index(arrow)) + 1].flip()


#generates a random list (solved)
def generate_rand_list(length):
    rand_color = {0: 'white', 1: 'red', 2: 'blue', 3: 'yellow'}
    return [Arrow((rand_color[random.randrange(4)]), True) for i in range(length)]


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
    if arrow.color == color_dict['yellow']:
        yellow_flip(arrows, arrow)


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
