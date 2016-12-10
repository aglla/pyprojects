#Hangman text game. (Made as a learning exercise; too difficult to play). This is my attempt to create a more concise
#hangman script than the one on http://inventwithpython.com/chapter9.html


import random
# Hangman ASCII art taken from http://inventwithpython.com/chapter9.html by Albert Sweigart
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
   \  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#create a list of words to randomly choose from
wordList = "edition ring product awarded museum innovation computer fedora cloud solar universe jupiter saturn asteroid light stapler highlighter pencil serial".split()

def getWord(wordList):
    #get a random number as the index in wordList
    randIndex = random.randint(0,len(wordList)-1)
    return randIndex

def displayBoard(HANGMANPICS, word, failed_guesses, correct_guesses):
    #display the current status of hangman and the word
    print(HANGMANPICS[len(failed_guesses)])
    hidden = '_ ' * len(word)
    currentWord = word
    for x in range(0, len(word)):                 #if the current index letter is not in the correct_guesses list, replace with '_', to hide the letter
        if word[x] not in correct_guesses:
            currentWord = currentWord.replace(word[x], '_ ')
    print(currentWord)   
    

def main():
    print("Hangman")
    randIndex = getWord(wordList)
    word = str(wordList[randIndex])
    failed_guesses = ''
    correct_guesses = ''
    displayBoard(HANGMANPICS, word, failed_guesses, correct_guesses)
    guess = ''
    playAgain = 'yes'
    while (True):   
        guess = str(input("Enter your guess: "))
        while (len(guess) != 1 or (guess.isalpha()==False)):  #if it's multiple letters or not a letter, ask again
            guess = str(input("Invalid, enter a single letter: "))
        if (len(failed_guesses) >= 5):
            displayBoard(HANGMANPICS, word, failed_guesses, correct_guesses)
            print("Y O U   L O S E!", " >>The correct word is", word)
            playAgain = str(input("Play Again? Type 'yes' or 'no': "))
            if playAgain != 'yes':
                quit()           #terminate
            else: main()         #restart program from main
        elif (guess in word):
            correct_guesses += guess
            displayBoard(HANGMANPICS, word, failed_guesses, correct_guesses)
        else:
            failed_guesses += guess
            displayBoard(HANGMANPICS, word, failed_guesses, correct_guesses)
main()        


    
    
    





        

