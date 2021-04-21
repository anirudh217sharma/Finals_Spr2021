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

# https://www.vertex42.com/ExcelTips/unicode-symbols.html LINK TO FIND THE SYMBOLS

sign1 = '\u2227'
sign2 = '\u2228'

rows = ['<', '>']
cols = [sign1, sign2]

# inverted greater than and less than unicode representation
# cell above is less than cell below : \u2227
# cell below is greater than cell above : \u2228

# This is the difficulty level for the puzzle

level = ['easy', 'medium', 'hard']


def space_check(grid):
    """
    :return A boolean representing whether there are any spaces left on the board
    :param grid: 4 x 4 numpy array
    :param position: coordinate of the space
    :return:
    """
    return '' in grid


def possible_choice(grid):
    """
    :param grid: a numpy array representing the existing stage of the game
    :return: possible moves for the existing chance : a list of tuples
    """
    move = np.where(grid == '')
    return list(zip(*move))


def initial_grid(m, level):
    """

    :param m: size of the grid : e.g 4 * 4
    :param level : difficulty level of the puzzle
    :return: A Randomly generated unsolved unequal puzzle

    """
    size = m + (m - 1)
    grid = np.zeros((size, size))
    grid: ndarray = np.where(grid == 0, 'E', 'E')

    # '@' means that the upper digit is greater
    # '#' means that the lower digit is greater
    # 'x' in the final grid signifies that the cell is useless without clues

    row_iterator = list(range(1, m, 2))

    for i in range(1, size, 2):

        arr1 = grid[i, :]  # row

        arr2 = grid[:, i - 1]  # column

        _ = list(range(1, size, 2))

        if 4 <= m < 6:

            arr1[random.choice(_)] = random.choice(rows)

            arr2[random.choice(_)] = random.choice(cols)
        elif 6 <= m <= 7:
            arr1[random.choice(_)] = random.choice(rows)
            arr1[random.choice(_)] = random.choice(rows)

            arr2[random.choice(_)] = random.choice(cols)
            arr2[random.choice(_)] = random.choice(cols)
        elif m >= 8:
            arr1[random.choice(_)] = random.choice(rows)
            arr1[random.choice(_)] = random.choice(rows)
            arr1[random.choice(_)] = random.choice(rows)

            arr2[random.choice(_)] = random.choice(cols)
            arr2[random.choice(_)] = random.choice(cols)
            arr2[random.choice(_)] = random.choice(cols)

        grid[i, :] = arr1

        grid[:, i - 1] = arr2

    """ Comment the below section if you are willing to view the display board  function 
        If that's the case then all the empty cells avaialble would be represented by 'E'
        otherwise always use the below code : All empty spots in the numpy array are represented by 
        ' ' and all the E's are spots which are not of any significance
    
    """
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if row % 2 == 0 and col % 2 == 0:
                grid[row][col] = ''
            else:
                if grid[row][col] == 'E':
                    grid[row][col] == 'X'

    #  adding a random numbers to the puzzle

    number = list(range(1, m + 1))  # possible numbers to fill

    indices = possible_choice(grid)  # list of position of the actual baord

    if level == 'hard':
        pass
    elif level == 'medium':
        random.shuffle(number)
        idx = len(number)
        for _, num in enumerate(number):
            choice = random.choice(indices)
            num = random.choice(number)
            grid[choice] = str(num)
            if _ >= idx / 3:
                break
    else:
        for _, num in enumerate(number):
            choice = random.choice(indices)
            grid[choice] = str(num)

    # verifying the inequalities less than greater than

    for num in range(1, size, 2):
        row = grid[num, :]
        for i, item in enumerate(row):
            if item == '<' or item == '>':
                grid[num, i] = 'E'
                grid[num - 1, i] = item

    return grid


board = initial_grid(4, level='medium')

# Sometimes the unequalities are not set up correctly


"""
So suppose a grid is of size 4 * 4 it would be represented as a 7 * 7 grid with the alternative 
rows and columns would represent the actual grid while the the intermediate rows and columns will store 
the clues if possible or otherwise be empty 

"""

"""
DISPLAY BOARD FUNCTION IS JUST FOR PRINTING INTO THE CONSOLE : DEBUGGING PURPOSES
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


# display_board(board)

# When the board is displayed inequality clues are represented and empty spaces are represented as 'E' , these
# will be replaced by digits during the solution

# TO DO : add one or two random number somewhere in the puzzle by replacing one of the valid spaces

# Working on the Solver

def testing_grid():
    """
    :return: returns a couple of testing grid from the link https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/unequal.html
             along with there solutions to verify and debug how the solver is working
        """

    test_puzzle = np.array([['2', 'E', '', 'E', '', 'E', ''],
                            [sign1, 'E', 'E', 'E', 'E', 'E', 'E'],
                            ['', 'E', '', 'E', '', 'E', ''],
                            ['E', 'E', 'E', 'E', sign2, 'E', sign2],
                            ['', 'E', '', '<', '', 'E', ''],
                            ['E', 'E', 'E', 'E', 'E', 'E', 'E'],
                            ['', 'E', '', 'E', '', 'E', '4']], dtype='str')  # 4 x 4
    return test_puzzle


# Backtracking Algorithm : Recursion to solve

# For each empty square the program would need a function to see if the choice is valid or not

def is_valid(grid, pos, choice):
    """
    :param grid: the current board state
    :param pos: position on the board which the player chooses
    :param choice: a number between 0 and the size of grid
    :return: A boolean
    """
    valid = True
    # Checking whether the number is in the same row

    row_check = list(grid[pos[0], :])
    col_check = list(grid[:, pos[1]])

    if str(choice) in row_check:
        valid = False

    # Checking whether the number is not in the same column

    if str(choice) in col_check:
        valid = False

    # updating the grid with the new value
    grid[pos] = str(choice)

    row_check = list(grid[pos[0], :])
    col_check = list(grid[:, pos[1]])

    # Satisfying the inequalities

    for num in range(1, len(row_check) - 1):
        if row_check[num - 1] != '' and row_check[num + 1] == '':
            if row_check[num] == '<':
                if int(row_check[num - 1]) > int(row_check[num + 1]):
                    valid = False
            elif row_check[num] == '>':
                if int(row_check[num - 1]) < int(row_check[num + 1]):
                    valid = False

    for num in range(1, len(col_check) - 1):
        # print(num)
        if col_check[num - 1] != '' and col_check[num + 1] != '':
            if col_check[num] == sign1:
                print(int(col_check[num - 1]), int(col_check[num + 1]))
                if int(col_check[num - 1]) > int(col_check[num + 1]):
                    valid = False
            elif col_check[num] == sign2:
                if int(col_check[num - 1]) < int(col_check[num + 1]):
                    valid = False

    return valid


# Valid function : Sanity check

# print(is_valid(test_puzzle, (0, 2), 2), 'Expected Value : False') # row check
# print(is_valid(test_puzzle, (2, 0), 2), 'Expected Value : False') # col check
# print(is_valid(test_puzzle, (2, 0), 3), 'Expected Value : True')  # checking vertical inequalities
# print(is_valid(test_puzzle, (4, 4), 1), 'Expected Value : True')  # checking vertical inequalities
# print(is_valid(test_puzzle, (4, 2), 2), 'Expected Value : False')  # checking vertical inequalities

test_puzzle = testing_grid()

print(possible_choice(test_puzzle))
moves = possible_choice(test_puzzle)
