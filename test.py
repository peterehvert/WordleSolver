#---------------------------------------------------------#
# import the entire Webster's dictionary
import json
from unittest import skip
dictionary = json.load(open('dictionary_compact.json'))
#---------------------------------------------------------#

#---------------------------------------------------------#
# save list of words that are only five letters
def CreateDictionary(dictionary):

    listOfWords = []
    for word in dictionary:
        if len(word) == 5:
            listOfWords.append(word)
    sortedDict = sorted(listOfWords)
    return sortedDict

def CreateAnswers(sortedDict):
    #---------------------------------------------------------#
    goodGuesses = []
    # loop through every word in the dictionary
    for word in sortedDict:
        # start word as a valid guess
        guess = 1

        # loop through every letter in the word
        for i in range(0, 5):

            # if the letter in the word is a locked letter or not known in the solution, continue
            if ( ( (word[i] == lockedLetters[i]) or (lockedLetters[i] == '-') ) ):

                # if the letter is in the list of eliminated letters, disqualify the word
                if ( word[i] in eliminatedLetters):
                    guess = 0
                    break

                else:
                    # loop through every known letter
                    for knownLetter in knownLetters:
                        #if the word does not have one of the known letters in it, disqualify the word
                        if knownLetter not in word:
                            guess = 0
                            break
                        
                        else:
                            guess = 1

            else:
                guess = 0
                break 
        
        if guess == 1:
            goodGuesses.append(word)

    return goodGuesses

def ScoreAnswers(goodGuesses):
    scores = []
    for guess in goodGuesses:
        score = 0
        for i in range(0,5):
            for otherGuess in goodGuesses:
                if guess[i] == otherGuess[i]:
                    score += 2

                elif guess[i] in otherGuess:
                    score += 1

        scores.append(score)
    return scores

#---------------------------------------------------------#


#---------------------------------------------------------#
# ask for user input
lockedLetters = input('Enter locked letters: ')
knownLetters = input('Enter known letters: ')
eliminatedLetters = input('Enter eliminated letters: ')
#---------------------------------------------------------#

#---------------------------------------------------------#
# run the code
sortedDict = CreateDictionary(dictionary)
possibleWords = CreateAnswers(sortedDict)
scores = ScoreAnswers(possibleWords)

guessDict = {}
for guess, score in zip(possibleWords, scores):
    guessDict[guess] = score


sortedGuesses =  sorted(guessDict.items(), key=lambda kv: (kv[1], kv[0]))

for key, value in sortedGuesses:
    print (key + ": " + str(value))


#---------------------------------------------------------#