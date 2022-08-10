def find_next_empty(puzzle):
    #finds the next (row, col) on the puzzle that's not filled yet --> rep with -1
    #return (row,col) tuple [or (None,None) if there is none]

    # keep in mind that we are using 0-8 for our indices
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    
    return None, None

def is_valid(puzzle, guess, row, col):
    #figures out whether the guess at (row,col) is valid
    # returns True if valid, False if not

    #let's start w/ the row:
    row_vals = puzzle[row]
    if guess in row_vals:
        return False #number can only show up once in the row

    #now the columns:
    # col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i][col]) #goes through each row at the same col location
    col_vals = [puzzle[i][col] for i in range(9)] # does the above in one line!
    if guess in col_vals:
        return False

    #now the 3x3 square matrixes:
    #find where we want the 3x3 to start
    # iterate over the 3 values in the row/col
    row_start = (row // 3) * 3 # 1//3 = 0 | 5//3 = 1, ...
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    
    #if we get pass all of these checks, then valid
    return True

def solve_sudoku(puzzle):
    #solve sudoku using BACKTRACKING
    #our sudoku itself is a list of list
    #each inner list is a row in our sudoku puzzle
    #return whether a solution exists
    #mutates puzzle to be the solution if it does exist

    #Step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    #Step 1.1: if there's nowhere left, we are done bc we only allow valid inputs
    if row is None:
        return True

    #Step 2: if there is a place to put a number, then make a guess between 1-9
    for guess in range(1,10):
        #Step 3: check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            #Step 3.1: if valid, the place the guess in the puzzle
            puzzle[row][col] = guess

            #now recurse using the new, mutated puzzle
            #Step 4: recursively call our function
            if solve_sudoku(puzzle):
                return True

        #Step 5: if not valid OR if our guess does not solve the puzzle, then we need to
        # back track and try a new number
        puzzle[row][col] = -1 #reset the guess

    #Step 6: if none of the numbers that we try work, puzzle is UNSOLVABLE
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
    print(solve_sudoku(example_board))
    print(example_board)