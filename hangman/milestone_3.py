
def check_guess(guess):
        guess = guess.lower()
        if guess in word_list:
         print(f"Good guess! {guess} is in the word.") 
        else:
            print(f"Sorry, {guess} is not in the word. Try again")


def ask_for_input():    
    while True:
           guess = input("Please guess a letter")
           if guess.isalpha():
               check_guess(guess) 
               break
           else: 
               print("Invalid letter. Please, enter a single alphabetical character.")

ask_for_input()