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

Firstly , it would ask the user to select a difficulty level: 

![image](https://user-images.githubusercontent.com/48274485/116638145-4d453080-a92b-11eb-9885-ea6856c532b2.png)

Secondly, it would ask you to choose a grid size :
![image](https://user-images.githubusercontent.com/48274485/116638195-6bab2c00-a92b-11eb-8790-d26bc053bffb.png)

After this it would show a surface which has a button to play the game and another to solve the game: 

![image](https://user-images.githubusercontent.com/48274485/116638340-c775b500-a92b-11eb-89ca-15344dbfe7ae.png)

Clicking on the play button will generate a random puzzle of the selected grid size and difficulty as follows : 

![image](https://user-images.githubusercontent.com/48274485/116638435-f3913600-a92b-11eb-8c3e-736ced5d457b.png)

Users at this point are expected to solve the game, an interactive UI is still in progress which can allow the users to fill the boxes with numbers as they go along. 

By clicking the Solve Game button at any point would show you the Unique solution. 

![image](https://user-images.githubusercontent.com/48274485/116638629-571b6380-a92c-11eb-9f7d-2e87771a0b7e.png)


Time Complexity Analysis : 

TO-DO

