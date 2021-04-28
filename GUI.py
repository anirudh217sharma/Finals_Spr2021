# TODO : Better color combination for the UI
# TODO : GUI breaks for m > 5 fix that


sign1 = '\u2227'
sign2 = '\u2228'

from typing import Any, Union
from Widget import *
import pygame, sys
import time
from pygame_functions import *

from Unequal import *

# pygame initialization

pygame.init()

# Dimensions of the gameplay screen
height = 800
width = 800
Line_width = 10

from pygame.rect import Rect
from pygame_gui.elements.ui_text_entry_line import UITextEntryLine

"""
NOTE : PYGAME COORDINATE SYSTEM IS SET UP IN A WAY LIKE FOLLOWS :
     The origin is at the top left corner , and (800,800) is on the bottom right corner 
     Always leave the area from (0,0) - (200,200) for interactive widgets and gameplay features 
"""



# COLORS FOR THE SCREEN
LIGHTPURPLE = (153, 0, 153)
Red = (255, 0, 0)
Background = (28, 170, 156)
Line_color = (23, 145, 135)
SHADOW = (192, 192, 192)
LIGHTBLUE = (0, 0, 255)
LIGHTGREEN = (0, 255, 0)
YELLOW = (100, 100, 0)

# Button colors

red = (200, 0, 0)
green = (0, 200, 0)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

# screen = pygame.display.set_mode((height, width))
pygame.display.set_caption('Unequal Puzzle')
""""  Asking the user for the game size and the Difficulty level"""
import pygame as pg

clock = pg.time.Clock()
screen = pg.display.set_mode((640, 480))
pygame.display.set_caption('Unequal Puzzle')

COLOR_INACTIVE = (100, 80, 255)
COLOR_ACTIVE = (100, 200, 255)
COLOR_LIST_INACTIVE = (255, 100, 100)
COLOR_LIST_ACTIVE = (255, 150, 150)

level = DropDown(
    [COLOR_INACTIVE, COLOR_ACTIVE],
    [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
    50, 50, 200, 50,
    pg.font.SysFont(None, 30),
    "Select Difficulty", ["Hard", "Medium",'Easy'])

grid_size = DropDown(
    [COLOR_INACTIVE, COLOR_ACTIVE],
    [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
    100, 50, 200, 50,
    pg.font.SysFont(None, 30),
    "Select Grid size", ["4",'5','6','7'])

l = None
m = None
run = True
loop = True
while run:
    clock.tick(5)

    event_list = pg.event.get()
    for event in event_list:
        if event.type == pg.QUIT:
            run = False

    selected_option_1 = level.update(event_list)
    if selected_option_1 >= 0:
        level.main = level.options[selected_option_1]
        l = level.options[selected_option_1]

    screen.fill((255, 255, 255))
    level.draw(screen)
    pg.display.flip()
    if l is not None:
        while loop:
            clock.tick(5)

            event_list = pg.event.get()
            for event in event_list:
                if event.type == pg.QUIT:
                    loop = False

            selected_option_1 = grid_size.update(event_list)
            if selected_option_1 >= 0:
                grid_size.main = grid_size.options[selected_option_1]
                m = int(grid_size.options[selected_option_1])

            screen.fill((0, 0, 0))
            grid_size.draw(screen)
            pg.display.flip()

            if m is not None:
                run = False
                loop = False
                game = True


screen = pygame.display.set_mode((height, width))
pygame.display.set_caption('Unequal Puzzle')
screen.fill(YELLOW)

# This is the difficulty level for the puzzle

level = l.lower()

# Drawing a line

# pygame.draw.line(screen, Red, (10, 10), (300, 300))
game_size = 2 * m - 1
base_font = pygame.font.Font("seguisym.ttf", 32)

from Unequal import *

horizontal_length = 800
vertical_length = 600

# representing the grid in rectangles (which are squares)

vertical_cell_size = vertical_length / game_size
horizontal_cell_size = horizontal_length / game_size


def draw_grid(grid):
    """
    :param grid : the puzzle board
    :return: a representation of the board on the game screen
    """
    # horizontal line

    m = int((grid.shape[0] + 1) / 2)
    game_size: Union[int, Any] = 2 * m - 1

    # grid = initial_grid(m, level='easy')

    # Testing the button for the 4 x 4 grid
    top_left = (0, 200)
    top_right = (800, 200)

    bottom_left = (0, 800)
    bottom_right = (800, 800)

    horizontal_length = 800
    vertical_length = 600

    # representing the grid in rectangles (which are squares)

    vertical_cell_size = vertical_length / game_size
    horizontal_cell_size = horizontal_length / game_size

    # text objects

    for row, num in enumerate(list(range(5, 800, int(horizontal_cell_size)))):
        for col, idx in enumerate(list(range(205, 800, int(vertical_cell_size)))):
            try:
                pygame.draw.rect(screen, (255, 255, 255),
                                 pygame.Rect(num, idx, int(horizontal_cell_size), int(vertical_cell_size)), width=5)
                text = grid[col, row]
                if text == '>' or text == '<' or text == sign1 or text == sign2:
                    pygame.draw.rect(screen, SHADOW,
                                     pygame.Rect(num, idx, int(horizontal_cell_size), int(vertical_cell_size)))

                if text != 'E':
                    text_surface = base_font.render(text, True, (0, 0, 0))
                    if m <= 5:
                        screen.blit(text_surface,
                                    (num + int(horizontal_cell_size / 3), idx + int(vertical_cell_size / 3)))
                    else:
                        screen.blit(text_surface,
                                    (num + int(horizontal_cell_size / 5), idx + int(vertical_cell_size / 5)))

                else:
                    pygame.draw.rect(screen, SHADOW,
                                     pygame.Rect(num, idx, int(horizontal_cell_size), int(vertical_cell_size)))

            except IndexError:
                break


# Working on the providing users an option to display the text in the grid , also includes connecting the
# numpy game board with the screen

global SolutionList
SolutionList = []
# red circles means that these are invalid boxes and have no significance whatsoever
if m < 6:
    puzzle, solution = game(m=m, level=level)
else:
    flag = str(random.choice(list(range(49))))
    os.chdir(r'C:\Users\aniru\PycharmProjects\A2-Spr2021\Finals_Spr2021\6x6')
    with open('puzzle' + flag  +'.npy', 'rb') as f:
        puzzle = np.load(f)
    with open('solution' + flag +'.npy', 'rb') as f:
        solution = np.load(f)

os.chdir(r'C:\Users\aniru\PycharmProjects\A2-Spr2021\Finals_Spr2021')
# main loop , this is always necessary in Pygame
# grid_text = ''
# GRID_SELECT = base_font.render('Please enter the size of the game :', True, (255, 255, 255))
# screen.blit(GRID_SELECT, (100, 0))
#
# level_text = ''
# Level_select = base_font.render('Please enter the level among easy,medium or hard', True, (255, 255, 255))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        """Button interaction - when someone clicks on the button it gives the solution
           if they click on it again the problem is redisplayed from the start"""

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                mouse = pygame.mouse.get_pos()
                if 50 + 200 > mouse[0] > 50 and 20 + 80 > mouse[1] > 20:
                    draw_grid(solution)
                if 500 + 200 > mouse[0] > 500 and 20 + 80 > mouse[1] > 20:
                    draw_grid(puzzle)

        mouse = pygame.mouse.get_pos()

        # Adding a button to solve and play the game
        if 500 + 200 > mouse[0] > 500 and 20 + 80 > mouse[1] > 20:
            pygame.draw.rect(screen, (160, 160, 160), (500, 20, 200, 80))
        else:
            pygame.draw.rect(screen, (192, 192, 192), (500, 20, 200, 80))

        # print(mouse)

        if 50 + 200 > mouse[0] > 50 and 20 + 80 > mouse[1] > 20:
            pygame.draw.rect(screen, (160, 160, 160), (50, 20, 200, 80))
        else:
            pygame.draw.rect(screen, (192, 192, 192), (50, 20, 200, 80))

        solve_surface = base_font.render('Solve Game', True, (0, 0, 0))
        screen.blit(solve_surface,
                    (70, 40))

        play_surface = base_font.render('Play Game', True, (0, 0, 0))
        screen.blit(play_surface, (520, 40))

    pygame.display.update()

# https://www.geeksforgeeks.org/how-to-create-buttons-in-a-game-using-pygame/
