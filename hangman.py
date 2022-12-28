import os
import pickle
import random

# python 3.8.10
# a cli hangman app

# add/remove words from wordlist
default_wordlist = [ 
    "banana", "fish", "skyscraper",
    "book", "glasses", "pencil", 
    "photo", "umbrella", "water",
    "violet"
]

def create_wordlist():
    # This function creates a file and 
    # dumps the list 'default_wordlist'
    # to it the file and closes it
    file_object = open('wordlist.pydata', 'wb')
    pickle.dump(default_wordlist, file_object)
    file_object.close()

def open_wordlist():
    # This function loads words from a file and 
    # returns it
    file_object = open('wordlist.pydata', 'rb')
    words = pickle.load(file_object)
    file_object.close()
    return words

def load_words():
    # Try to store loaded words into the list, 'words'.
    # If the file doesn't exist, it creates a new file
    # and dumps the list 'default_wordlist' instead
    try: 
        words = open_wordlist()
        return words
    except Exception:
        create_wordlist()
        words = open_wordlist()
        return words

def display_title_bar():
        # Clear the terminal screen, and display a title bar
        os.system('clear')
        print("----------------------------------")
        print("--- Hangman - Words stored: %s" % len(words))
        print("----------------------------------")
        print("--- Lives Left: %d" % lives)
        print("----------------------------------")

def get_user_choice():
    user_guess = input("Guess [a-z, Q]: ")
    if user_guess != "Q":
        user_guess = user_guess.lower()
    return user_guess

def quit():
    print("\nThe word was %s." % random_word)
    print("Thanks for playing, bye-bye!")
    choice = "Q"
    return choice

# End of functions
# Initialize variables

# Check for any modifcations to 'default_wordlist'.
# If the list was modifed, overwrite 
# old wordlist and replace it
words = load_words()
if len(words) != len(default_wordlist):
    create_wordlist()
    words = load_words()

choice = " "
lives = 7
wrong_guesses = []
random_word = random.choice(words)
random_letters = list(random_word)
display_word = [0] * len(random_letters)
got_user_input = False

# Main program
display_title_bar()
while choice != "Q":
    display_title_bar()

    # Display wrong guesses made by the user
    print("Wrong guesses: ", end="")
    for wrong_guess in wrong_guesses:
        print("%s, " % wrong_guess, end="")
    print("")

    if lives == 0:
        choice = quit()
        break

    # Check for correct user input/guess
    skip = True
    for index, letter in enumerate(random_letters):       
        correct_guess = choice in random_letters
        if correct_guess and choice == random_letters[index]:
            display_word[index] = choice

    # Display underscores or letters
    print("\n>>> ", end="")
    for index, letter in enumerate (display_word):
        if display_word[index] != 0:
            print("%s " % letter, end="")
        else:
            print("_ ", end="")

    # Test if user has fully guessed the word
    player_win = 0 in display_word
    if player_win is False:
        print("\n\nYou win!")
        choice = quit()
        break
    print("\n")

    # Get user input
    choice = (get_user_choice())
    got_user_input = True
    
    # Terminate app mid-game
    if choice == "Q":
            quit()
            
    # Reduce lives for incorrect user input
    wrong = choice not in random_letters
    deducted = choice in wrong_guesses
    if deducted:
        continue
    elif wrong and got_user_input:

        lives -= 1
        wrong_guesses.append(choice)    
