import random
from re import A #need random to get random word
import string
from words import words #importing the words list from words.py

#some words in the list have '-' or ' ' which we cannot guess in hangman
#we must filter those out first
def get_valid_word(words):
    word = random.choice(words) #randomly choose word from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_word(words).upper()
    word_letters = set(word) #turn the word we got into a set
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #words that the user has guessed
    lives = 6

    while len(word_letters) > 0 and lives > 0: #keep playing while word is not guessed
        #used letters and lives
        #' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('you have used these letters: ', ' '.join(used_letters))
        print(f'Lives: {lives}')

        #current word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        #get user input
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter) #add that letter to the used letter set
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1 #subtract lives if wrong guess

        elif user_letter in used_letters:
            print('You have already guessed that letter. Try another character.')
        
        else:
            print('Invalid character. Please guess a letter.')
        
        print(' ')
    
    #get here once lives = 0 or word guessed
    if lives == 0:
        print(f'You died, word was: {word}')
    else:
        print(f'You win! Word was: {word}')

hangman()