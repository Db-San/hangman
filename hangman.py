import os
import pickle
import random

# Python 3.8.10
# A CLI Hangman app
# Bonus: Make the CLI app pretty

# This can be changed.
default_wordlist = [ 
    "banana", "fish", "skyscraper",
    "book", "glasses", "pencil", 
    "photo", "umbrella", "water",
    "alcohol"
]

def create_wordlist():
    # This function creates a file and dumps the list 'default_wordlist'
    #  into a file.
    file_object = open('wordlist.pydata', 'wb')
    pickle.dump(default_wordlist, file_object)
    file_object.close()

def open_wordlist():
    # This fnction loads words from a file and returns it.
    file_object = open('wordlist.pydata', 'rb')
    words = pickle.load(file_object)
    file_object.close()
    return words

def load_words():
    # This function loads words from a file for the game to choose from.
    #  It puts them in the list 'words'. If the file doesn't exist, 
    #  it creates the file and dumps pre-defined words into the file.
    try: 
        words = open_wordlist()
        return words
    except Exception:
        create_wordlist()
        words = open_wordlist()
        return words

def display_title_bar():
        # Clears the terminal screen, and displays a title bar.
        os.system('clear')
        print("*******************************************")
        print("*** Hangman - Words stored: %s\t\t***" % len(words))
        print("*******************************************")
        print("*** Lives Left: %d\t\t\t***" % lives)
        print("*******************************************")
def get_user_choice():
    user_guess = input("Guess [a-z, Q]: ")
    return user_guess

def quit():
    print("Thanks for playing, bye.")
    choice = "Q"
    return choice

# Main app

# Initialize Variables
words = load_words()

# Check for any changes in the default_wordlist. If the file was
# modifed, it will overwrite the old file and replace it with the
# new 'default_wordlist'
if len(words) != len(default_wordlist):
    create_wordlist()
    words = load_words()

choice = " "
lives = 7
random_word = random.choice(words)
random_letters = list(random_word)
display_word = [0] * len(random_letters)

# Start the game
display_title_bar()
while choice != "Q":
        
    # Check if the user has enough lives yet to continue
    if lives == 0:
        print("No more lives left! Game Over!")
        print("The word was %s." % random_word)
        choice = quit()
        break
    
    display_title_bar()

    # Display underscores or letter. Reduces lives accordingly
    skip = True 
    for index, letter in enumerate(random_letters):
        if choice in choice == random_letters[index]:
            display_word[index] = choice
        if choice not in random_letters and skip:
            lives -= 1
            skip = False

    print("\n>>>\t", end="")
    for index, letter in enumerate (display_word):
        if display_word[index] != 0:
            print("%s " % letter, end="")
        else:
            print("_ ", end="")
    
    # Check if the user has guessed the word
    player_win = 0 in display_word
    if player_win is False:
        print("\n\nYou win!")
        choice = quit()
        break

    print("\n")
    # Get user input
    choice = (get_user_choice())