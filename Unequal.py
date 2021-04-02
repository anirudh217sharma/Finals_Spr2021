"""
Name : Unequal (Puzzle)

Fill in the grid with numbers from 1 to the grid size, so that every number appears exactly once in each row and column, and so that all the < signs represent true inequalities (i.e. the number at the pointed end is smaller than the number at the open end).

A valid puzzle must have at least a single row or column or a diagonal in numerical order. There is no constraints on the corners.

As a result now there is not restriction to work on a 4 * 4 grid so the implementation would be for a general n * n grid.
"""

import numpy as np
from numpy.core._multiarray_umath import ndarray
import random

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
        print(i)
        arr1 = grid[i, :]  # row

        arr2 = grid[:, i]  # column

        _ = list(range(1, size, 2))

        arr1[random.choice(_)] = random.choice(rows)
        arr2[random.choice(_)] = random.choice(cols)

        grid[i, :] = arr1
        grid[i, :] = np.where(grid[i, :] == 'E', 'X', grid[i, :])
        grid[i, :][0] = 'E'
        grid[i, :][-1] = 'E'

        grid[:, i] = arr2
        grid[:, i] = np.where(grid[:, i] == 'E', 'X', grid[:, i])
        grid[:, i][0] = 'E'
        grid[:, i][-1] = 'E'

    print(grid)

    return grid


initial_grid(4)
