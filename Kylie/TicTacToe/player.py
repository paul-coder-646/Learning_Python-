import math
import random 

class Player:
    def __init__(self, letter):
        # letter is either x or o
        self.letter = letter
    
    # we want all players to get their next move given a game
    def get_Move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_Move(self, game):
        return random.choice(game.available_moves())

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_Move(self, game):
        valid_square = False
        val = 0
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        
        return val

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_Move(self, game):
        if len(game.available_moves()) == 9: # we have to start the game, so choose randomly
            return random.choice(game.available_moves())
        else:
            # get the square based off the minimax algorithm
            square = self.minimax(game, self.letter)['position']
            return square

    def minimax(self, state, player):
        max_player = self.letter # yourself
        other_player = 'O' if player == 'X' else 'X' # the other player 

        # first check if last move was a winner
        # base case for recursion
        if state.current_winner == other_player:
            # return position and score for minimax to work
            return {'position': None,
            'score': 1 * (state.num_empty_squares() + 1) 
            if other_player == max_player 
            else -1 * (state.num_empty_squares() + 1)}
        
        elif not state.empty_squares(): # Well if nobody won, then we must have a tie
            return {'position': None, 'score': 0}

        # Initialisation of dictionaries (THESE ARE THE ONES THAT WE RECURSIVELY OPTIMISE)
        if player == max_player:
            best = {'position': None, 'score': -math.inf} # We want to maximise our score so if best is init to -math.inf, then always greater values exist
        
        else:
            best = {'position': None, 'score': math.inf} # We want to minimse the opponents score so if best is init to math.inf, then always lower values exist
        
        # check all the moves that are possible from that point on in the game
        for possible_move in state.available_moves():

            # step 1: make a random move
            state.make_move(possible_move, player)

            # step 2: recurse using minimax to simulate the game after that move
            sim_score = self.minimax(state, other_player)

            # step 3: undo that move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            # step 4: update the dictionaries if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score # replace best

            else:
                if sim_score['score'] < best['score']:
                    best = sim_score # replace worst :D
                
        return best
                    



            

