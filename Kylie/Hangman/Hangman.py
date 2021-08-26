from Learning.Kylie.Hangman.Hangman_Words import words
import random, time, string

def get_valid_word(words):
    # choose a random word from the Wordlist to play on
    word = random.choice(words)
    #check if word is valid
    while "-" in word or ' ' in word:
        word = random.choice(words)

    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 5
    # Pseudoword is used to give the Player the Position of the letters already guessed right in the word with "_" where he
    # Has not yet been able to guess the correct letter
    pseudoword = ""


    while word_letters != [] and lives > 0:
        print(f"Your used letters are: {', '.join(used_letters)}")
        for i in word_letters:
            if i in used_letters:
                pseudoword = pseudoword + i
            else:
               pseudoword = pseudoword + "_"

        print(f"To give you mere mortal hint :D {pseudoword}")
        user_input = (input("Guess a letter of the word:")).upper()

        # Add Letter to ued letters only if the letter is nt yet used
        if user_input in alphabet - used_letters:
          used_letters.add(user_input)

        if user_input in word_letters:
            word_letters.remove(user_input)
            print(f"Yup, the letter {user_input} is in the word !")
            # Just a timer to model a more player like behavior from the computer
            time.sleep(1)

        elif user_input in used_letters:
            lives = lives - 1
            print(f"You already tried {user_input}, Pick another one")
            time.sleep(1)

        else:
            lives = lives - 1
            print(f"It appears, {user_input} is not a valid input (A-Z,a-z), Pick another one")
            time.sleep(1)

    if lives == 0:
        print("Sorry, out of tries")
    elif word_letters == []:
        print(f"Congrats, {word} was the word, You nailed it !")

if __name__ == '__main__':
    hangman()