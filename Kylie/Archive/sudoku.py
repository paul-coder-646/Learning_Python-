from pprint import pprint

def find_next_empty(puzzle):
    # finds the next empty space in the puzzle thats not filled yet

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    
    return None, None # If we arrive here, there is apparently no space left

def is_valid(puzzle, guess, row, col):
    # figure out whether the guess at the row/col is a valid sudoku move.
    # returns true if it is and false if it isn't

    # let's first check the row
    row_values = puzzle[row]
    if guess in row_values:
        return False
    
    # lets do the column
    column_values = [puzzle[i][col] for i in range(9)]
    if guess in column_values:
        return False

    # finally let's check the 3x3 square
    # this devides the board into 9 3x3 boxes and we want to compute 
    # the first entry of the one we are curretnly in 

    row_start = (row // 3) * 3 
    # // ignores the remainder so e.g 5 // 3 = 1
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    
    # In case we end here, apparently we must have a valid guess so...
    return True


def solve_sudoku(puzzle):
    # solve sudoku using backtracking !
    # return whether a solution exists

    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # step 1.1: if there is nowhere left, then we're done as the puzzle is solved
    if row is None:
        return True

    # step 2: if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if this is valid, then place that guess on the puzzle!
            puzzle[row][col] = guess
        
            # now recurse using this (incrementally more solved) puzzle
            # step 4: recursively call our function
            if solve_sudoku(puzzle):
                return True # This is our base case, if we did the last move then we have nowhere to place so we are done
    
        # step 5: if not valid OR if our guess does not solve the puzzle, then we need to backtrack
        puzzle[row][col] = -1 # reset the guess, this is also the end of the road for "foul" recursion calls

    #step 6: if none of the numbers that we try work, then this puzzle is UNSOLVABLE !!!
    return False 

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    pprint(solve_sudoku(example_board))
    pprint(example_board)

