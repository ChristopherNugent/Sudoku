# Sudoku
A Sudoku solving program written in Python that uses logic and recursive backtracking to solve any solvable Sudoku puzzle of any size.

# Usage
The primary class in this solution is the SudokuTable class, which holds both the data and logic for a Sudoku puzzle. 

Puzzles are read into the class by a serial, which represents the entire puzzle as a string. The order of the characters is starts from the top left corner, and proceeds left to right, top to bottom. Valid characters are 0 for empty slots, and 1-9,a-z,A-Z in that order as valid "answer" characters. This larger character range allows for larger puzzles, up to 49x49 puzzles, with larger tables being simply a matter of expanding the BaseConverter class to support a larger base.

Puzzles are created with `puzzle = SudokuTable(serial)`, and the solution (if it exists) can be generated with `solution = SudokuTable.guessSolve(puzzle)`. If there is no solution, -1 will be returned.

# Todo
+ Convert into working module. 
+ Add more logical solving tools, such as unique possibles within a subset.
