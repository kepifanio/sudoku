# sudoku
Written by: Katherine Epifanio

Purpose:
        This program solves a sudoku puzzle using a Constraint
        Satisfaction Problem approach with Conflict-Directed
        Backtracking.

Files Included:
        sudoku.py           -   Contains all of the source code.
        Test file directory

Compiling & Usage:
        python sudoku.py [FILENAME]

        The program requires 1 text file argument containing the
        sudoku puzzle to be solved. If the file contents are not
        formatted correctly or if the puzzle's contents violate the
        constraints of the sudoku puzzle (regarding repeated numbers
        in rows, columns, or squares), then the program quits.
        If more than one argument is provided or if the provided
        argument cannot be read, the program quits.

        Example Input File Format:

        6 0 8 7 0 2 1 0 0
        4 0 0 0 1 0 0 0 2
        0 2 5 4 0 0 0 0 0
        7 0 1 0 8 0 4 0 5
        0 8 0 0 0 0 0 7 0
        5 0 9 0 6 0 3 0 1
        0 0 0 0 0 6 7 5 0
        2 0 0 0 9 0 0 0 8
        0 0 6 8 0 5 2 0 3
