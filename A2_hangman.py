# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"


def loadWords():
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
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    true = 0
    false = 0
    for char in secretWord:
        if char in lettersGuessed:
            true += 1
        else:
            false += 1
    if false == 0:
        return True
    else:
        return False
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...

# When you've completed your function isWordGuessed, uncomment these three lines
# and run this file to test!

#secretWord = 'apple'
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(isWordGuessed(secretWord, lettersGuessed))

# Expected output:
# False


def getGuessedWord(secretWord, lettersGuessed):
    answer = []
    for char in secretWord:
        if char in lettersGuessed:
            answer.append(char + ' ')
        else:
            answer.append(' ')
    return' '.join(answer)

    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...


# When you've completed your function getGuessedWord, uncomment these three lines
# and run this file to test!

#secretWord = 'apple'
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(getGuessedWord(secretWord, lettersGuessed))

# Expected output:
# '_ pp_ e'


def getAvailableLetters(lettersGuessed):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for value in lettersGuessed:
        alpha.remove(value)
    return ' '.join(alpha)

    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # Hint: You might consider using string.ascii_lowercase, which
    # is a string comprised of all lowercase letters.

    # FILL IN YOUR CODE HERE...


# When you've completed your function getAvailableLetters, uncomment these two lines
# and run this file to test!

#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(getAvailableLetters(lettersGuessed))

# Expected output:
# abcdfghjlmnoqtuvwxyz


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many 
      letters the secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    # sets number of guesses player has in game (10 guesses)
    guessLeft = 10
    
    # keeps track of all of the letters guessed
    lettersGuessed = [ ]
    
    # k provides the length of the word that is being guessed (secret word)
    k = len(secretWord)
    
    # This section will print the game introduction while telling the person playing what the length of the word is
    print (str('Welcome to the game, Hangman!'))
    print (str('I am thinking of a word that is ' + str(k) + ' letters long.'))
    print (str('-------------'))
    
    # guessLeft > 0 will signify that the player still has at least one guess left
    while guessLeft > 0:
        
        # this code will print the number of guess that remain
        print (str('You have ' + str(guessLeft) + ' guesses left.'))
        
        # print the letters that are still available
        print (str('Available letters: ') + getAvailableLetters(lettersGuessed))
        
        # print/ request the user to guess a letter
        guess = input('Please guess a letter: ')
        
        # quality check to ensure that the letter is in the lowercase form
        guessLower = guess.lower()
        
        # this code will add the letter just entered to the list of lettersGuessed
        lettersGuessed.append(guessLower)
        
        # This will prompt a message telling the player if they have entered a letter that they have previously guessed
        if lettersGuessed.count(guessLower) > 1:
            print(str("Oops! You've already guessed that letter: ") + getGuessedWord(secretWord, lettersGuessed))
            print(str('-------------'))
        
        # tells the user if the letter they guessed is in the secretWord, shows progress which will include the guess (getGuessedWord function)
        elif guessLower in secretWord:
            print(str('Good guess: ') + getGuessedWord(secretWord, lettersGuessed))
            print(str('-------------'))
            
            # Print congrats when the person guesses the entire secret word and break will signify the end of the code 
            if isWordGuessed(secretWord, lettersGuessed) == True:
                return str('Congratulations, you won!')
                break
        # if the letter entered is not correct, decrease # of guessLeft by 1 and show (getGuessedWord function)
        else:
            guessLeft -= 1
            print(str('Oops! That letter is not in my word: ') + getGuessedWord(secretWord, lettersGuessed))
            print(str('-------------'))
    # if there are no more guesses (guessLeft = 0) inform the user that they are out of guesses.
    else:
        return(str('Sorry, you ran out of guesses. The word was ' + str(secretWord) + '.'))

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)