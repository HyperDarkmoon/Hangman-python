import random
from wordlist import words
import string
import hangmangraphics

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_word(words).upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6


    while len(word_letters) > 0 and lives >  0:

        print('You have',lives,' lives and You have used these letters', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                hangmangraphics.draw_hangman(lives+1)
                print('this letter is not int the word')


        elif user_letter in used_letters:
            print('You have used that character before')

        else: 
            print("invalid character, try again")
    
    if lives == 0:
        print('You didnt guess the word, it was: ',word)     
    else:
        print('You guessed it, the word is: ',word,'!')

hangman()