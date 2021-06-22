--------------------------------------------------------------------------------------------------------
Sudoku is a puzzle game that is typically played on a 9x9 board. The goal of the game is to 
fill every row, column and 3x3 square with a number 1-9. None of the numbers can be repeated in its
respective row, column or 3x3 square.

The algorithm is used to verify whether the user's solution is the correct solution. It first checks
every row to see if there are any duplicate numbers, then every column and finally every 3x3 sqaure.

This is a very simple console based sudoku game. The board and inputs are all handled in the console.
There is currently only one game board, but future versions can have puzzles randomly generated.

--------------------------------------------------------------------------------------------------------
To run the program: open the directory where file is located then type "python3 (filename)" in the command line
To enter a number into a cell, follow the row and column headers.

EX) ab1 will put the number 1 in row a column b.
    This is case-insensitive.

The game will tell you automatically if you solved the puzzle.