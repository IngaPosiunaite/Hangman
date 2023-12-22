import random

from hangman864.hangman.milestone_3 import check_guess

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list 
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = []  
        self.num_letters = num_letters 
        self.list_of_guesses = []


    def check_guess(guess):
        guess = guess.lower()
        if guess in word:
            print(f"Good guess! {guess} is in the word.") 
        else:
            print(f"Sorry, {guess} is not in the word. Try again")
        for i in range(len(word)):
            if word[i] == guess:
                word_guessed[i] = guess
                num_letters -=1
            else:
                num_lives -= 1
                print("Sorry," + guess + "is not in the word")
                print("You have" + str(num_lives) + "lives left")



    def ask_for_input():    
        while True:
           guess = input("Please guess a letter")
           if not guess.isalpha() or len(guess) != 1: 
               print("Invalid letter. Please, enter a single alphabetical character.")
           elif guess in list_of_guesses:
            print("You alreadytried that letter!")
           else: 
               check_guess(guess) 
               list_of_guesses.append(guess)
               break
           

ask_for_input()