#Command line minesweeper using Recursion and Classes

import random
import re

#create a board Object to represent the game
#"create new board object", "dig here", "render game for this object", etc
class Board:
    def __init__(self, dim_size, num_bombs):
        #lets keep track of these parameters
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        #create the board
        #helper function!
        self.board = self.make_new_board() #plant bombs
        self.assign_values_to_board()

        #initalize a set to keep track of which locations we've uncovered
        #we'll save (row,col) tuples into this set
        self.dug = set() #if we dig at (0,0), then self.dug = {(0.0)}
    
    def assign_values_to_board(self):
        #now that bombs are planted, we assign number 0-8 for all the empty spaces,
        # which represents how many neighboring bombs there are. we can precompute
        # these and it'll save us some effort checking what's around the board later on
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue # if there's already a bomb, dont calculate anything
                self.board[r][c] = self.get_num_neighboring_bombs(r,c)

    def get_num_neighboring_bombs(self, row, col):
        #let's iterate through each of the neighboring positions and sum number of bombs
        # top left: (row-1, col-1)
        # top middle: (row-1, col)
        # top right: (row-1, col+1)
        # left: (row, col-1)
        # right: (row, col+1)
        # bottom left: (row+1, col-1)
        # bottom middle: (row+1, col)
        # bottom right: (row+1, col+1)

        #make sure we do not go out of bounds!
        num_neighboring_bombs = 0
        for r in range(max(0, row - 1), min(self.dim_size - 1, (row + 1)) + 1):
            for c in range(max(0, col - 1), min(self.dim_size - 1, (col + 1)) + 1):
                if r == row and c == col:
                    #our original location, don't check
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1
        
        return num_neighboring_bombs

    def dig(self, row, col):
        #return True if successful dig, False if bomb

        #a few scenarios:
        # dig bomb -> game over
        # dig at location with neightboring bombs -> finish dig
        # dig at location with no neighboring bombs, recursively dig neighbors!

        self.dug.add((row,col)) #keep track of where we have dug

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        
        #self.board[row][col] == 0 case
        for r in range(max(0, row - 1), min(self.dim_size - 1, (row + 1)) + 1):
            for c in range(max(0, col-1), min(self.dim_size - 1, (col + 1)) + 1):
                if (r, c) in self.dug:
                    continue #already dug here, no need to dig again
                self.dig(r, c)

        #if our inital dig didn't het a bomb, we shouldn't hit a bomb here
        return True

    def __str__(self):
        #this is a magic funciton where if you call print on this object,
        # it'll print out what this funcito returns!
        #so lets return a string that shows the board to the player

        #first let's create a new array that represents what the user would see
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug: # if we have dug there, show it
                    visible_board[row][col] = str(self.board[row][col])
                else: #else keep it hidden
                    visible_board[row][col] = ' '
        
         # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep


    def make_new_board(self):
        #construct a new board based on the dim_size and num_bombs
        #we should construct the list of lists here

        #generate a new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        #this creates an array like this:
        # [[None, None, ..., None],
        #  [None, ..., None, None],
        #  [..., None, None, None]]
        #this is the representation of our board

        #plant bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':
                #we already have a bomb in this location, so keep going
                continue

            board[row][col] = '*' #plant the bomb here
            bombs_planted += 1
        
        return board


def play(dim_size = 10, num_bombs = 10):
    #step 1: create the board and plant bombs
    board = Board(dim_size, num_bombs)

    #step 2: show user the board and ask for where they want to dig
    #step 3a: if location is a bomb, show game over message
    #step 3b: if location is not a bomb, dig recursively until each square
    #         is at least next to a bomb
    #step 4: repeat staps 2 and 3 until no more places to dig

    safe = True

    while len(board.dug) < board.dim_size ** 2 - num_bombs: #loop while there are digable spaces
        print(board)
        #re.split is a regex split
        # it splits the user input by comma (,) and whitespace (\\s), no matter how many spaces (*)
        # ex. 0,0 | 0, 0 | 0,   0 | ...
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: "))
        row, col = int(user_input[0]), int(user_input[-1]) #0 for first item, -1 for last item

        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            #check if user has inputed something outside our board space
            print("Invalid location, Try again.")
            continue

        #if valid, dig
        safe = board.dig(row, col)

        if not safe: #safe == False
            #bomb dug
            break
        
    #2 ways the while loop ends
    if safe:
        print("CONGRAGULATIONS! MINES SWEPT!")
    else:
        print('BOOM! GAME OVER!')
        #reveal whole board to player
        #dig up the whole board with this double for loop
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]

        #show board
        print(board)

if __name__ == '__main__': #good practice, only runs if you run the .py directly
    play()