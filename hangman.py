import os
import pickle
import random

# Python 3.8.10
# A CLI Hangman app

# Wordlist for the game. Can be modified
default_wordlist = [ 
    "banana", "fish", "skyscraper",
    "book", "glasses", "pencil", 
    "photo", "umbrella", "water",
    "violet"
]

def create_wordlist():
    # This function creates a file and dumps the list 'default_wordlist'
    #  into it
    file_object = open('wordlist.pydata', 'wb')
    pickle.dump(default_wordlist, file_object)
    file_object.close()

def open_wordlist():
    # This fnction loads words from a file and returns it
    file_object = open('wordlist.pydata', 'rb')
    words = pickle.load(file_object)
    file_object.close()
    return words

def load_words():
    # This function loads words from a file for the game to choose from.
    #  It then puts them in the list 'words'. If the file doesn't exist, 
    #  it creates the file and dumps the list 'default_wordlist'
    #  into the file.
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
        print("**********************************")
        print("*** Hangman - Words stored: %s" % len(words))
        print("**********************************")
        print("*** Lives Left: %d" % lives)
        print("**********************************")

def get_user_choice():
    user_guess = input("Guess [a-z, Q]: ")
    return user_guess

def quit():
    print("Thanks for playing, bye.")
    choice = "Q"
    return choice

# Main app
# Initialize variables
words = load_words()

# Check for any changes in the list 'default_wordlist'. If the list was
#  modifed, it will overwrite the old wordlist file and replace it with the
#  modified list
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

# Start the game
display_title_bar()
while choice != "Q":
    display_title_bar()

    # Check if the user has enough lives to continue
    if lives == 0:
        print("\nNo lives left! Game Over!")
        print("The word was %s." % random_word)
        choice = quit()
        break

    # Display wrong guesses made by the user
    print("Wrong guesses: ", end="")
    for wrong_guess in wrong_guesses:
        print("%s, " % wrong_guess, end="")
    print("")

    # Check if the user guess is correct
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

    # Check if the user has guessed the word
    player_win = 0 in display_word
    if player_win is False:
        print("\n\nYou win!")
        choice = quit()
        break
    print("\n")

    # Get user input
    choice = (get_user_choice())
    got_user_input = True

    # Check if user input is wrong, then reduce lives accordingly
    wrong = choice not in random_letters
    deducted = choice in wrong_guesses
    if deducted:
        continue
    elif wrong and got_user_input:
        lives -= 1
        wrong_guesses.append(choice)    
