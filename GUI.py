import pygame, sys
import time

from Unequal import *

grid = initial_grid(4)

# pygame initialization

pygame.init()

# Dimensions of the gameplay screen
height = 800
width = 800
Line_width = 10

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

# Drawing a line

# pygame.draw.line(screen, Red, (10, 10), (300, 300))
m = 5
grid = initial_grid(m)


def draw_lines(m):
    """

    :param m : size of the square grid
    :return:
    """
    # horizontal line

    game_size = 2 * m - 1

    top_left = (0, 200)
    top_right = (800, 200)

    bottom_left = (0, 800)
    bottom_right = (800, 800)

    horizontal_length = 800
    vertical_length = 600


    # drawing horizontal lines
    counter = 0
    for num in range(game_size):
        pygame.draw.line(screen, Line_color, (0, 200 + counter), (800, 200 + counter), Line_width)
        counter += vertical_length / game_size

    # drawing vertical lines
    counter = 0
    for num in range(game_size):
        pygame.draw.line(screen, Line_color, (game_size + counter, 200), (game_size + counter, 800), Line_width)
        counter += horizontal_length / game_size


draw_lines(m)

# main loop , this is always necessary in Pygame

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
