from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None # keep track of potential winner

    def print_board(self):
        # just getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range (3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' 'in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):  # if valid move, then make the move (assign square to letter) then return true. if invalid, return false
        
        if self.board[square] == ' ':
            self.board[square] = letter

            if self.winner(square, letter): # Has the player won on that specific move ? 
                self.current_winner = letter

            return True
        else:
            return False
    
    def winner(self, square, letter):
        row_ind = square // 3 # Inverse function to modulus...How often does 3 fit into the square we chose
        row = self.board[row_ind*3 : (row_ind +1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        col_ind = square % 3 # Plain Mod Function. Gives remainder of square / 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0: # The diagonals always consist of even numbers
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True

            diagonal2 = [self.board[j] for j in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

def play(game, x_player, y_player, print_game=True):

    letter = 'X' # Starting letter

    while game.empty_squares():

        if print_game and letter == 'X': # In case the Human Plays, give him the board for orientation 
            game.print_board_nums()

        if letter == 'O': # To make it feel a little bit more human, when the computer plays
            time.sleep(1)

        if letter == 'O':
            square = y_player.get_Move(game)
            # Get the Moves of the Players ready. The moves are NOT yet taken
        else:
            square = x_player.get_Move(game)
        
        # Take the moves if they are allowed!
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('') # just empty line
        
        # Winner?
        if game.current_winner:
            if print_game:
                print(letter + ' wins!')
                return letter # In case we got a winner, this winner must have been the last player so current letter is the winner

        letter = 'O' if letter == 'X' else 'X' #change the players

    # This is only relevant, if no winner has been found and no space is left on the board
    if print_game:
        print('Its a tie!')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    y_player = GeniusComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, y_player, print_game=True)