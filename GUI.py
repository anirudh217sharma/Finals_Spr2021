# TODO : Better color combination for the UI

from typing import Any, Union

import pygame, sys
import time

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

Red = (255, 0, 0)
Background = (28, 170, 156)
Line_color = (23, 145, 135)

screen = pygame.display.set_mode((height, width))
pygame.display.set_caption('Unequal Puzzle')
screen.fill(Background)

# This is the difficulty level for the puzzle

level = ['easy', 'medium', 'hard']

# Drawing a line

# pygame.draw.line(screen, Red, (10, 10), (300, 300))
m = 4

game_size = 2 * m - 1

def draw_grid(m):
    """

    :param m : size of the square grid
    :return:
    """
    # horizontal line

    game_size: Union[int, Any] = 2 * m - 1

    grid = initial_grid(m, level='easy')

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

    base_font = pygame.font.Font(None, 32)

    for row, num in enumerate(list(range(5, 800, int(horizontal_cell_size)))):
        for col, idx in enumerate(list(range(205, 800, int(vertical_cell_size)))):
            pygame.draw.rect(screen, Line_color,
                             pygame.Rect(num, idx, int(horizontal_cell_size), int(vertical_cell_size)), width=5)
            text = grid[col, row]
            text_surface = base_font.render(text,True,Red)
            screen.blit(text_surface, (num+int(horizontal_cell_size/2),idx + int(vertical_cell_size/2)))
            
    print(grid)
    # Working on the providing users an option to display the text in the grid , also includes connecting the
    # numpy game board with the screen


draw_grid(m)


# main loop , this is always necessary in Pygame

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_X = event.pos[0]
            mouse_Y = event.pos[1]

    pygame.display.update()
