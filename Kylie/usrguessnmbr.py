import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x} ! : "))

        if((guess < 1) | (guess > x)):
            print("Not within range, try again")
            continue
        elif(guess < random_number):
            print("Too low, try again")
            continue
        
        elif(guess > random_number):
            print("Too high, try again")
            continue

    print("Congrats, you got it right :D")
        
if __name__ == '__main__':
    guess(6)