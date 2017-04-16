import re, os


def displayBoard():
    i = 0
    os.system('clear')
    print("\n    Remaining guesses: "+str(guessesRemaining))
    print("    ["+", ".join(str(x) for x in lettersGuessed)+"]")
    print("    "+displayWord)
    print("            _____")
    if guessesRemaining < 6:
        print("            O    |")
    else:
        print("                 |")
    if guessesRemaining < 3:
        print("           /|\   |")
    elif guessesRemaining < 4:
        print("           /|    |")
    elif guessesRemaining < 5:
        print("            |    |")
    else:
        print("                 |")
    if guessesRemaining < 5:
        print("            |    |")
    else:
        print("                 |")
    if guessesRemaining < 1:
        print("           / \   |")
    elif guessesRemaining < 2:
        print("           /     |")
    else:
        print("                 |")
    print("                 |")
    print("        _________|")


def isGuessInWord(guess):
    global displayWord

    i = 0
    while i < len(keyWord):
        if guess.lower() == keyWord[i].lower():
            if i == 0:
                displayWord = keyWord[i] + displayWord[i+1:]
            elif i == len(keyWord)-1:
                displayWord = displayWord[:i] + keyWord[i]
            else:
                displayWord = displayWord[:i] + keyWord[i] + displayWord[i+1:]
        i += 1
    return guess.lower() in displayWord.lower()


def getGuess():
    while True:
        guess = input("    Please, guess a letter: ")
        if guess.isalpha() and len(guess) == 1 and guess not in lettersGuessed:
            break
        else:
            print("    Either your input is invalid or you have already guessed that letter. Please, try again.")
    return guess


def playHangman():
    global guessesRemaining
    global lettersGuessed

    while guessesRemaining > 0:
        displayBoard()
        guess = getGuess()
        if not isGuessInWord(guess):
            guessesRemaining -= 1
            lettersGuessed += guess
        if "*" not in displayWord:
            break
    displayBoard()
    # win or lose
    if guessesRemaining > 0:
        print("\n\n    Congratulations! You've won.")
    else:
        print("\n\n    Sorry, you've lost.")
    print("    The word/phrase was \"" + keyWord + "\"")


# main game loop
while True:
    keyWord = input("Enter word for your friend to guess: ")
    displayWord = re.sub('[a-zA-Z]', '*', keyWord)
    guessesRemaining = 6
    lettersGuessed = []
    playHangman()

    # play again?
    ans = ""
    while True:
        ans = input("    Play again?(yes/no) ")
        if ans.lower() == "yes" or ans.lower() == "no":
            break
    if ans == "no":
        break

