# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    count = 0
    for i in secret_word:
        for n in letters_guessed:
            if i == n:
                count += 1
    return True if count == len(secret_word) else False

def get_guessed_word(secret_word, letters_guessed):
    current_word = []
    if len(letters_guessed) == 0:
        return "_ " * len(secret_word)
    for i in secret_word:
        for n in letters_guessed:
            if i == n:
                current_word.append(i)
                break
            elif n == letters_guessed[-1]:
                current_word.append("_ ")
    return "".join(current_word)



def get_available_letters(letters_guessed):
    return "".join(sorted(set(string.ascii_lowercase).difference(set(letters_guessed))))



def hangman(secret_word):
    guesses = 6
    letters_guessed = []
    warnings = 3
    print(f'''Welcome to the game Hangman!
I am thinking of a word that is {len(secret_word)} letters long.
You have 3 warnings left.''')
    while guesses > 0:
        print(f"""{"-"*13}
You have {guesses} guesses left.
Available letters: {get_available_letters(letters_guessed)}""")
        entered_symbol = input("Please guess a letter: ").lower()
        if entered_symbol.isalpha() and get_available_letters(letters_guessed).__contains__(entered_symbol):
            letters_guessed.append(entered_symbol)
            if secret_word.__contains__(entered_symbol):
                print("Good guess: ", end = "")
            else: 
                if ["a", "e", "i", "o", "u"].__contains__(entered_symbol):
                    guesses -= 2
                else:
                    guesses -= 1
                print("Oops! That letter is not in my word: ", end = "")
        else: 
            if not entered_symbol.isalpha():
                print("Oops! That is not a valid letter. ", end = "")
                warnings -= 1
            else:
                print("Oops! You've already guessed that letter. ", end = "")   
                warnings -= 1
            if warnings >= 0:
                print(f"You have {warnings} warnings left: ", end ="")
            else:
                print("You have no warnings left so you lose one guess: ", end ="")
                guesses -= 1
        print(get_guessed_word(secret_word, letters_guessed))
        if is_word_guessed(secret_word, letters_guessed):
            break
    print("-"*13)
    if guesses != 0:
        print("""Congratulations, you won!
Your total score for this game is: """, guesses*len(set(secret_word)))
    else:
        print(f"Sorry, you ran out of guesses. The word was {secret_word}.")


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(' ', '') 
    for i in range(len(other_word)):
        try:
            if my_word[i] == "_" or (other_word[i] not in set(my_word) and my_word[i] == other_word[i]):
                pass
            else:
                return False
        except IndexError:
            return False
    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_matches = []
    for i in wordlist:
        if match_with_gaps(my_word, i):
            possible_matches.append(i)
    if len(possible_matches) == 0:
        print("No matches found")
    else:
        print(i for i in possible_matches)



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses = 6
    letters_guessed = []
    warnings = 3
    print(f'''Welcome to the game Hangman!
I am thinking of a word that is {len(secret_word)} letters long.
You have 3 warnings left.''')
    while guesses > 0:
        print(f"""{"-"*13}
You have {guesses} guesses left.
Available letters: {get_available_letters(letters_guessed)}""")
        entered_symbol = input("Please guess a letter: ").lower()
        if entered_symbol.isalpha() and get_available_letters(letters_guessed).__contains__(entered_symbol):
            letters_guessed.append(entered_symbol)
            if secret_word.__contains__(entered_symbol):
                print("Good guess: ", end = "")
            else: 
                if ["a", "e", "i", "o", "u"].__contains__(entered_symbol):
                    guesses -= 2
                else:
                    guesses -= 1
                print("Oops! That letter is not in my word: ", end = "")
        elif entered_symbol == "*":
            print("Possible word matches are: ", show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
        else: 
            if not entered_symbol.isalpha():
                print("Oops! That is not a valid letter. ", end = "")
                warnings -= 1
            else:
                print("Oops! You've already guessed that letter. ", end = "")   
                warnings -= 1
            if warnings >= 0:
                print(f"You have {warnings} warnings left: ", end ="")
            else:
                print("You have no warnings left so you lose one guess: ", end ="")
                guesses -= 1
        print(get_guessed_word(secret_word, letters_guessed))
        if is_word_guessed(secret_word, letters_guessed):
            break
    print("-"*13)
    if guesses != 0:
        print("""Congratulations, you won!
Your total score for this game is: """, guesses*len(set(secret_word)))
    else:
        print(f"Sorry, you ran out of guesses. The word was {secret_word}.")




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #secret_word = input("secret word = ")
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
