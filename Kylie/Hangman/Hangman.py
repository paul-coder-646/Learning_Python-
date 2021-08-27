import string
import random
from Hangman_Words import words

def get_valid_word(words):
    word = random.choice(words) #randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word

def hangman():
    word = get_valid_word(words).upper()
    word = word.upper()
    word_letters = set(word)#letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed

    lives = 6

    print('Howdy :D I guess you know how it goes :) \n')
    while len(word_letters) > 0 and lives > 0:

        #show the player the already used words
        print(f'You have {lives} lives left and you already used these letters: ' + ' '.join(used_letters)) 

        #show the word but only the letters, the player already guessed (e.g H O - S E -> HOUSE)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper() #get user input for the letter and format everything upper case 
       
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter) #add letter to the used letters if the letter is not used so far

            if user_letter in word_letters: #remove all the correctly guessed letters from the word 
                word_letters.remove(user_letter)
                lives += 1
                print(' \n Correct :D on to the next one. I was so generous to give you one live back :D\n')
            else:
                print('\n I\'m sorry but that letter is not in the word D: \n')
                lives = lives - 1 # This means that the user guessed a wrong letter and thus looses one live

        elif user_letter in used_letters:
            print('\n You have already used that letter :P Try Again \n') #lives stay the same, otherwise its too hard
        
        
        else:
            print('\n Invalid character :D Don\'t worry, just try again \n')
            lives = lives - 1
    
    if lives == 0:
        print(f'I\m sorry, you died :/ But you can try again :D The word was {word} \n')
    
    else:
        print(f'Right the word was {word}. Congrats, you won :D \n')

    if input('Do you wanna play again ? y/n') == y:
        return hangman()
    else:
        return


if __name__ == '__main__':
    hangman()