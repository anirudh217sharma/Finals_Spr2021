# Finals_Spr2021

Unequal Puzzle : Fill in the grid with numbers from 1 to the grid size, so that every number appears exactly once in each row and column, and so that all the < signs 
represent true inequalities (i.e. the number at the pointed end is smaller than the number at the open end).

https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/unequal.html

Uneuqal puzzle variant : This is a new type of puzzle in which there is an additional constarint , which is atleast a single row ,column or any one of the longest 
diagonals should be in numerical order. 

NOTE : The numerical constaint can be in reverse order as well. So 1,2,3,4 nd 4,2,3,1 are both valid combinations for satisfying this constraint. 

There are two main files used here :

Unequal.py -> This uses a recursive approach to randomly generate puzzles of different grid sizes and difficulty level. 
GUI.py -> Provides an interactive display of the puzzle to the user based on the option they chose. At any point the user can ask for the solution of the puzzle. 

