# ohpe-projekti-code-or-die

CODE OR DIE MANUAL


Game Description

Welcome to our game! The purpose of this game is to move around in 
different rooms until you find the tutorial tasks, pass the final exam, and ultimately win the game.

Problem Analysis

The main problems we addressed in this game are:

Saving and reading game state
Reading input and handling errors
Implementing the rooms with functions, their calling, and saving and reading from a text file

Problem Solution

Our program starts by checking if loadfile.txt exists. If it does, it loads the existing recording 
of the game state by reading the room in question from the file and setting the player's position. 
If there is no file, then the default room is always room no. 1.

Every time the player moves from one room to another, the save() function is called, 
which saves that room in the loadfile.txt file. This allows the state of the saved game to be loaded 
when the game is opened again.

To move through the rooms, the roomchooser(room) function is used, which takes the current room 
as a parameter. The player must complete the tutorial tasks in room no. 3 and pick them up in a 
list called Inventory[] using the add_to_inventory function to get to the next room. 
In room no. 4, the player will be asked if they want to return the tutorial tasks using the print_inventory() 
function so they can take the exam in room no. 5. If the player answers the exam question correctly, 
they win the game; otherwise, they have to start over.

We also implemented error handling for user input. If the user does not enter the correct 
type of requested input, they will be prompted again using a while True loop until the correct input is given.

Operating instructions are printed for each room as the game progresses. 
If the game does not load for some reason, loadfile.txt must be deleted from the same folder where the code_or_die.py file is located.

How to Play

To start the game, run code_or_die.py. Follow the instructions on the screen to progress 
through the rooms and complete the tutorial tasks. Remember to save your game by completing the tasks in each room. 
If you answer the exam question correctly, you win the game! 
If you encounter any issues, please refer to the operating instructions for each room, and if necessary, 
delete loadfile.txt from the game folder to start over.
