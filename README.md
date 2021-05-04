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

Gameplay : 

Use the terminal : python GUI.py 

Firstly , it would ask the user to select a difficulty level and a grid size. 
Clicking on the play button will generate a random puzzle of the selected grid size and difficulty as follows : 

![image](https://user-images.githubusercontent.com/48274485/116638435-f3913600-a92b-11eb-8c3e-736ced5d457b.png)

Users at this point are expected to solve the game, an interactive UI is still in progress which can allow the users to fill the boxes with numbers as they go along. 

By clicking the Solve Game button at any point would show you the Unique solution. 

![image](https://user-images.githubusercontent.com/48274485/116638629-571b6380-a92c-11eb-9f7d-2e87771a0b7e.png)

I have used to solve functions one is called the solver which stops when it finds a new a solution and the main one is called the Solve function which keeps solving the grid until it finds a valid solution and then carries on and adds all possible solutions to a Solution list.

<b> Time Complexity Analysis for the main Solver function: </b> 

NOTE : An m x m  puzzle is represented by a (2m-1) x (2m-1) grid to take into account the inequalities. So the solver starts from the top left corner of the cell and starts filling the possible numbers. If the grid state is valid , it places that number and moves forward in the row. It carries on like this , unitl all possible solutions are found. 

The time complexity for a m x m puzzle which is represented by a 2m-1 x 2m-1 grid should be O(m^3m)  which can be simplied to O(m^m) because 3 can be ignored as a constant. Because although the grid is represented by a larger number there are 3 for loops which have maximum of m iterations possible. 



