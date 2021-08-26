import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f"I guess the number is: {guess}. Too high (h) too low (l) or correct (c)?").lower()

        if feedback == "h":
            high = guess - 1

        elif feedback == "l":
            low = guess + 1


    print("Yay I did It :D")


computer_guess(2021)