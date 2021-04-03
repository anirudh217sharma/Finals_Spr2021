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

    rows = ['<', '>']
    cols = ['@', "#"]

    for i in range(1, size, 2):

        arr1 = grid[i, :]  # row

        arr2 = grid[:, i]  # column

        _ = list(range(1, size, 2))

        arr1[random.choice(_)] = random.choice(rows)

        arr2[random.choice(_)] = random.choice(cols)

        grid[i, :] = arr1

        grid[:, i] = arr2

    return grid


board = initial_grid(4)
print(board)
"""
So suppose a grid is of size 4 * 4 it would be represented as a 7 * 7 grid with the alternative 
rows and columns would represent the actual grid while the the intermediate rows and columns will store 
the clues if possible or otherwise be empty 

"""

def display_board(board):
    """

    :param board: current board configuration
    :return: displays the board
    """
    s = ''
    for num in range(0,board.shape[0]):
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


    print(s)


display_board(board)

