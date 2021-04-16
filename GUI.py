import pygame, sys
import time

from Unequal import *

grid = initial_grid(4)

# pygame initialization

pygame.init()

# Dimensions of the gameplay screen
height = 800
width = 800
Line_width = 15

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


def draw_lines(height ,width):
    """

    :param height: height of the grid
    :param width: width of the grid
    :return:
    """
    # horizontal line
    pass


# draw_lines()


# main loop , this is always necessary in Pygame

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
