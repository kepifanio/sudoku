# Written by: Katherine Epifanio

import sys
row, col = (9, 9)
puzzle = [[0 for i in range(col)] for j in range(row)]
domain = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Prints current state of sudoku board.
def print_board(puzzle):
    for x in range(9):
        print("      ", end = "")
        for y in range(9):
            print(puzzle[x][y], end = " ")
        print("\n", end = "")
    print()


# Reads inputted file and stores contents of sudoku board. Program
# exits if file cannot be read or if initial puzzle violates the
# sudoku constraints.
def store_board(filename):
    try:
        file = open(filename)
        row = 0
        for line in file:
            line = line.replace(" ", "")
            line = line.strip('\n')
            col = 0
            for char in line:
                puzzle[row][col] = int(char)
                col += 1
            row += 1
    except:
        sys.exit("\nCannot read file '" + filename + "'\n")


# Drives actual solving of board by recursion. If the entire domain
# for possible sudoku values has been traversed with no solution found
# at a given index, a failure message is returned.
def solve(puzzle):
    # If there are no blank spots left, return current board
    if not find_blank(puzzle):
        return puzzle
    else:
        blank_loc = find_blank(puzzle)
        x = blank_loc[0]
        y = blank_loc[1]
        # Runs through all possible values (1-9). To improve efficiency
        # each index would have its own domain which is updated as the 
        # board environment changes.
        for value in domain:
            # Check if value can be put here without violating constraints
            if(constraint_check(puzzle, value, blank_loc)):
                puzzle[blank_loc[0]][blank_loc[1]] = value
                solution = solve(puzzle)
                if solution != "NO SOLUTION FOUND":
                    return solution

                # If solution wasn't returned, backtrack
                puzzle[blank_loc[0]][blank_loc[1]] = 0

    # Reaching this points means all attempts have been exhausted
    # and no solution was found
    return "NO SOLUTION FOUND"


# Iterates through board to find next available blank spot to fill.
def find_blank(puzzle):
    for x in range(9):
        for y in range(9):
            if puzzle[x][y] == 0:
                return [x, y]
    return False


# Checks if the presence of a certain value at a certain index will
# comply with the sudoku constraints. If this returns false, the
# program will be prompted to backtrack (or will indicate an invalid
# inputted puzzle if called by solvable function).
def constraint_check(puzzle, value, indices):
    row = indices[0]
    col = indices[1]

    # Check row
    for y in range(9):
        if y != col:
            if puzzle[row][y] == value and value != 0:
                return False
    # Check column
    for x in range(9):
        if x != row:
            if puzzle[x][col] == value and value != 0:
                return False

    # Check square
    row_start = row - (row % 3)
    col_start = col - (col % 3)
    for x in range(row_start, row_start + 3):
        for y in range(col_start, col_start + 3):
            sq_id = [x,y]
            if puzzle[x][y] == value and puzzle[x][y] != 0 and sq_id != indices:
                return False

    return True


# Calls the constraint_check function on every index of sudoku board
# to ensure that the intitial puzzle is in compliance with sudoku
# constraints.
def solvable(puzzle):
    for x in range(9):
        for y in range(9):
            if not constraint_check(puzzle, puzzle[x][y], [x, y]):
                return False
    return True


# Checks for correct number of command line arguments, calls
# check to see if puzzle is solvable, and then calls the solve
# function.
def main():
    if len(sys.argv) != 2:
        sys.exit("\nUsage: python sudoku.py [FILENAME]\n")
    else:
        filename = sys.argv[1]

    store_board(filename)
    if not solvable(puzzle):
        sys.exit("\nThe inputted puzzle violates the sudoku constraints\n")
    else:
        print("\n----Inputted Sudoku Puzzle----")
        print_board(puzzle)
        solution = solve(puzzle)
        print("\n    ------Solution------")
        print_board(solution)


main()
