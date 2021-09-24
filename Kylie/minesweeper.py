import re, random

# lets create a board object to represent the minesweeper game
# this is so that we can create instances of games or call functions on this object
class Board:
    def __init__(self, dim_size, num_bombs):
        #just initialize as we need the parametes later on
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # let's create the board
        # helper function
        self.board = self.make_new_board() # plant bombs
        self.assign_values_to_board()
        # initialize a set to keep track of which locations we've uncovered
        # we'll save (row,col) tuples into this set
        self.dug = set()

    def make_new_board(self):
        
        # construct a new board based on the dim size and the num bombs
        # we should construct the list of lists here 

        #gernate the new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        #plant the bombs 
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1) # just return a random integer that corresponds to board square
            row = loc // self.dim_size # rom -> how many times does my row size fit into the position 
            col = loc % self.dim_size # column -> what remains after we substract all rows we were able to fill completely

            if board[row][col] == '*': # check if we already have a bomb here, if so skip this position
                continue
            
            board[row][col] = '*' # plant the bomb
            bombs_planted += 1
        
        return board

    def assign_values_to_board(self):
        # now we have planted all the boards, we assign a number 0-8 for all empty spaces
        # representing hom many neighboring bombs are there. This is a precomputation so we don't 
        # have to re-compute it after every move
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*': # that means we have found a bomb but these squares are irrelevant as game over as soon as one of those is stepped on
                    continue

                self.board[r][c] = self.get_num_neighboring_bombs(r, c) # get num of nearby bombs
        
    def get_num_neighboring_bombs(self, row, col):
        # lets iterate through all neighboring positions
        # make sure we don't go out of bounds

        num_neigboring_bombs = 0
        for r in range(max(0, row-1),min(self.dim_size,(row+1)+1)): # the min and max function ensures that we stay inside array bounds :)
            for c in range(max(0, col-1),min(self.dim_size,(col+1)+1)):
                if r == row and c == col:
                    continue # we just found the position we called the function on :D Doesn't help us however

                if self.board[r][c] == '*':
                    num_neigboring_bombs+=1

        return num_neigboring_bombs

    def dig(self, row, col):
        # dig at location
        # return True if successful, False if bomb dug

        # possibilities
        # hit a bomb -> game over
        # neighboring bombs - > finish digging and expose neighboring bombs
        # no neighboring bombs -> call dig() recursively on all neighborss until neighboring bombs exist for recursive function call

        self.dug.add((row, col)) # we dont need to worry about duplicates even if (row, col) exists already as dug is a set

        if self.board[row][col] == '*':
                return False
        elif self.board[row][col] > 0: # Here our precomputing neighboring bombs becomes handy as we don't need to calculate it :)
                return True
            
        # self.board[row][col] == 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) in self.dug:
                    continue #we already dug there so skip
                    
                # this is the recursion part. Magic Happens here :D
                self.dig(r, c) 

        # if we haven't hit a bomb so far we should be good to go
        return True

    def __str__(self):
        # if we call print on the board object, this function returns a human readable version of it to us
        # here it return a string that shows the board to the players

        # first let's create a new array that represents what the what the user sees (only places where he dug already are visable)
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
            
        # now make it fancy and put it together in a nice string representation... 
        # (Code for the rest of this method directly copied from @kying18 as its really daunting to write as a beginner)
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



# play function for well, starting a play
def play(dim_size=10, num_bombs=10):
    # Step 1: create the playing board and plant the bombs
        board = Board(dim_size, num_bombs)

        # Step 2: show the user the board and ask for where they want to dig
        # Step 3a: if location is a bomb, show game over message -> return
        # Step 3b: if no more places to dig, VICTORY -> return
        # Step 4: if location is not a bomb then call play recursively, until at least each square 
        #         is next to a bomb

        while len(board.dug) < board.dim_size ** 2 - num_bombs:
            print(board)

            # ,(\\s)* is a regex that means a comma followed by any number of whitespaces that you want, 
            # e.g  1,1 -> [1, 1] ; 1,    1 -> [1, 1]
            user_input = re.split(',(\\s)*', input("where would you like to dig? Input as row,col eg. 1,1 : "))

            row, col = int(user_input[0]), int(user_input[-1]) # quick reminder: [-1] gives the last element of a list...

            # Mind you, exception handling for e.g ValueError and more input checks might be useful but we just hope we have a nice player :D
            if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
                print("Invalid location. Try again.")
                continue
            
            # if it's valid, we dig
            safe = board.dig(row, col)
            if not safe:
                # we dug a bomb :X
                break # rip game over

        # 2 ways this could end...
        if safe:
            print("\nCONGRATULATIONS!!!! YOU ARE A WINNER! :DDD")
        else:
            print("\nSORRY, GAME OVER. But you can try again :D")
            print("\nThe Board would have been:\n")
            # lets reveal the board so the user knows where he f***ed up :D
            board.dug = [(r, c) for r in range(board.dim_size) for c in range(board.dim_size)]
            # now all positions are in dug so should be made viewable by print()
            print(board)

if __name__ == '__main__':
    play()
        
    

    
