# youtuber = "dave2d"
# print("hello " + youtuber)
# print("hello {}".format(youtuber))
# print(f"hello {youtuber}")

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while (guess != random_number):
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry too low try again")
        elif guess > random_number:
            print("Sorry too high try again")
    print("Congrats you got it right ;D")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (H) or too low (L) or correct (C) ???").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print (f'Yay! The computer guessed your number, {guess}, correctly!')

def play():
    user = input("What's your choice ?: 'r' for rock 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'tie'

    if is_win(user, computer):
        return 'You won'
    return 'You lost!'


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())