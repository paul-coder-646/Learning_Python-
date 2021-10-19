import random

def rockpaperscissors():
    
    user = input('rock, paper or scissors ?: ')
    computer = random.choice(['rock','paper','scissors'])

    if user == computer:
        print('\n Its a Tie')
    elif is_win(user, computer):
        print('\n The Player won')
    else:
        print('\n The Computer won I\'m sorry')

    again = input('You wanna play again ? y/n: ')
    if (again == 'y'):
        return rockpaperscissors()
    else:
        return
    

def is_win(player, opponent):
    if (player == 'rock' and opponent == 'scissors') or (player == 'scissors' and opponent == 'paper') or (player == 'paper' and opponent == 'rock'):
        return True
    else:
        return False


if __name__ == '__main__':
    print(rockpaperscissors())

