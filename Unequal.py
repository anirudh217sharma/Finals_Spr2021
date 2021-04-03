"""
Name : Unequal (Puzzle)

Fill in the grid with numbers from 1 to the grid size, so that every number appears exactly once in each row and column, and so that all the < signs represent true inequalities (i.e. the number at the pointed end is smaller than the number at the open end).

A valid puzzle must have at least a single row or column or a diagonal in numerical order. There is no constraints on the corners.

As a result now there is not restriction to work on a 4 * 4 grid so the implementation would be for a general n * n grid.
"""

import numpy as np
from numpy.core._multiarray_umath import ndarray
import random
from termcolor import colored

"""
The grid can be represented as (m + (m-1) , m + (m-1)) for the empty rows and columns having the inequalities 
where necessary otherwise empty.

"""

rows = ['<', '>']
cols = ['@', "#"]


def initial_grid(m):
    """

    :param m: size of the grid : e.g 4 * 4
    :return: A Randomly generated unsolved unequal puzzle

    """
    size = m + (m - 1)
    grid = np.zeros((size, size))
    grid: ndarray = np.where(grid == 0, 'E', 'E')

    # '@' means that the upper digit is greater
    # '#' means that the lower digit is greater
    # 'x' in the final grid signifies that the cell is useless without clues

    for i in range(1, size, 2):

        arr1 = grid[i, :]  # row

        arr2 = grid[:, i - 1]  # column

        _ = list(range(1, size, 2))

        if 4 <= size < 6:

            arr1[random.choice(_)] = random.choice(rows)

            arr2[random.choice(_)] = random.choice(cols)
        elif 6 <= size <= 7:
            arr1[random.choice(_)] = random.choice(rows)
            arr1[random.choice(_)] = random.choice(rows)

            arr2[random.choice(_)] = random.choice(cols)
            arr2[random.choice(_)] = random.choice(cols)
        elif size >= 8:
            arr1[random.choice(_)] = random.choice(rows)
            arr1[random.choice(_)] = random.choice(rows)
            arr1[random.choice(_)] = random.choice(rows)

            arr2[random.choice(_)] = random.choice(cols)
            arr2[random.choice(_)] = random.choice(cols)
            arr2[random.choice(_)] = random.choice(cols)

        grid[i, :] = arr1

        grid[:, i - 1] = arr2

    return grid


board = initial_grid(4)

print(board)
print('------------------------')
"""
So suppose a grid is of size 4 * 4 it would be represented as a 7 * 7 grid with the alternative 
rows and columns would represent the actual grid while the the intermediate rows and columns will store 
the clues if possible or otherwise be empty 

"""


def display_board(board, color='cyan'):
    """
    :param board: current board configuration
    :return: displays the board
    """
    s = ''
    for num in range(0, board.shape[0]):
        arr = board[num, :]
        if num % 2 == 0:
            for idx in range(len(arr)):
                if idx % 2 == 0:
                    s += arr[idx] + '|'
                else:
                    if arr[idx] == 'E':
                        s += ' |'
                    else:
                        s += arr[idx] + '|'
        else:
            for idx in range(len(arr)):
                if arr[idx] == 'E':
                    s += ' |'
                else:
                    s += arr[idx] + '|'
        s += '\n'

        line_iterator = s.splitlines()

    game = []

    for idx in range(0, len(line_iterator) - 1, 2):
        end = line_iterator[idx]
        char = ''
        for i, j in zip(line_iterator[idx], line_iterator[idx + 1]):
            if i == 'E':
                char += i
            elif i == '|':
                char += i
            else:
                if j == '<' or j == '>':
                    char += j
                else:
                    char += i
        game.append(char)
    game.append(end)

    clue = []

    for idx in range(1, len(line_iterator), 2):
        clue.append(line_iterator[idx])

    for i, num in enumerate(clue):
        num = num.replace('<', ' ')
        num = num.replace('>', ' ')
        clue[i] = num

    clue.append('NA')

    game_state = ''

    for i, j in zip(game, clue):
        if j != 'NA':
            game_state += i
            game_state += '\n'
            game_state += j
            game_state += '\n'
        else:
            game_state += i
            game_state += '\n'

    print(colored(game_state, color, attrs=['bold']))


display_board(board)

# When the board is displayed inequality clues are represented and empty spaces are represented as 'E' , these
# will be replaced by digits during the solution

# To do : add one or two random number somewhere in the puzzle by replacing one of the valid spaces
