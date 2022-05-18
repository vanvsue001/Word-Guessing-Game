# Programming Project C || Python Development || CS 3270 || Brian Durney
# SueAnn Van Valkenburg
# 2/20/22

import random
import re

#get file
fileName = "words.txt"
#fileName = "wordtest.txt"
f = open(fileName, "r")
fileContents = f.readlines()

#get rid of newline
words = []
for content in fileContents:
    words.append(content.rstrip('\n').split(','))

#get user input
val = input("Enter the range of word lengths (low,high): ")
low = int(val[1])
high = int(val[3])

wordLens = list(range(low,high+1))
depth = high+1 - low
wordsLenList = depths = [[] for i in range(depth)]

#get all words of specified length
i = -1
for wordLen in wordLens:
    i+= 1
    for word in words:
        if len(word[0]) == wordLen:
            wordsLenList[i].append(word[0])
            

    

#select a short word all other words will start with
firstList = wordsLenList[0] 
randWord = random.choice(firstList) #choose one word have all words start with that word


#make sure all words in list start with selected word
depth = high+1 - low
#wordsSameStart = depths = [[] for i in range(depth)]
wordSameLetters = depths = [[] for i in range(depth)]
i = -1
#print('randWord: ', randWord)
for aList in wordsLenList:
    i += 1
    for word in aList: #need to get all words with conbintion of those letters
        temp = word
        randWordList = list(randWord)
        wordList = list(word)
        wordList.sort()
        randWordList.sort()
        
        if wordList == randWordList: 
            wordSameLetters[i].append(temp)
print('wordList: ', wordSameLetters)
                
        #if word.startswith(randWordFirstList) == True:
            #wordsSameStart[i].append(word)

#alphabetize sublists
for aList in wordSameLetters:
    aList.sort()

print(wordSameLetters)

    
def findWordToGuess():
    flattenedWordsSameStart = [item for sublist in wordSameLetters for item in sublist]
    #get one word with max length
    maxLength = []
    for word in flattenedWordsSameStart:
        if len(word) == (high+1):
            maxLength.append(word)
    if len(maxLength) != 0:
        wordToGuess = random.choice(maxLength)
            
    biggestWord =  ''
    if len(maxLength) == 0: #no word of max length then just pick longest word
        for word in flattenedWordsSameStart:
            if len(word) > len(biggestWord):
                biggestWord = word
    wordToGuess = biggestWord
    
    return wordToGuess
    

def scrambleLettersInWord(word):
    indLetters = list(word)
    scrambledWord = random.sample(word, len(word)) #returns a new shuffled list
    scrambledWord = random.sample(word, len(word))# make sure words really scrambled
    scrambledWord = ''.join(scrambledWord)
    if scrambledWord == word and len(word) != 1: #if scrambled word same as orginal rescramble
        if len(word) == 2:
            scrambledWord = word[1]+word[0]
        if len(word) == 3:
            scrambledWord = word[1]+word[0]+word[2]
        else:
            scrambleLettersInWord(word)
    return scrambledWord

def WordsIndex(word, list): #assumes list is list of lists
    i = -1
    for aList in list:
        i += 1
        #if(word[0] in aList):
        if(word in aList):
            index = aList.index(word)
            nestedIndex = [i,index]
            return nestedIndex

guessedWords = []
def addToGuessedWords(word):
    guessedWords.append(word)
    
def WordToGuess(wtg_wordsSameStart):
    flattenedWordsSameStart = [item for sublist in wtg_wordsSameStart for item in sublist]
    for wordG in guessedWords:
        if wordG in flattenedWordsSameStart:
            flattenedWordsSameStart.remove(wordG) #removes all words that have already been guessed
    if len(flattenedWordsSameStart) == 0: #all words have been guessed
        result = 'won'
    else:
        #randWordToGuess = random.choices(flattenedWordsSameStart)
        randWordToGuess = findWordToGuess()
        #print('fwtg: ', randWordToGuess)
        #scrammbledWordToGuess = scrambleLettersInWord(randWordToGuess)
        #guessedWords.append(randWordToGuess[0])
        #randWordToGuessValue = randWordToGuess[0]
        #index = WordsIndex(randWordToGuessValue, wtg_wordsSameStart)
        #result = [randWordToGuess, index]
        
        return randWordToGuess

depth = high+1 - low
underScoreWords = depths = [[] for i in range(depth)]
def startDisplay(list):
    i = -1
    for aList in list:
        i += 1
        for word in aList:
            str = "abcdefghijklmnopqrstuvwxyz"
            underscore = re.sub('[a-z]','_ ',word)
            underScoreWords[i].append(underscore)
    return underScoreWords

def updateDisplay(ud_wordToGuessAndIndex):
        nestedIndex = ud_wordToGuessAndIndex[1]
        firstIndex = nestedIndex[0]
        secondIndex = nestedIndex[1]
        correctWord = wordSameLetters[firstIndex][secondIndex]
        displayList[firstIndex][secondIndex] = correctWord
        printDisplay(displayList, wordSameLetters) #should display edited list

def checkGuess(guess, wordToGuessAndIndex):
        #print('WSL: ', wordSameLetters)
        #guess can match any guess in list 
        #cg_wordToGuessAndIndex = wordToGuessAndIndex
        #flatCGWordToGuess = [item for sublist in cg_wordToGuessAndIndex for item in sublist]
        #print('flatList: ', flatCGWordToGuess)
        #print(cg_wordToGuessAndIndex )
        #nestedIndex = wordToGuessAndIndex[1]
        #firstIndex = nestedIndex[0]
        #secondIndex = nestedIndex[1]
        #correctWord = wordSameLetters[firstIndex][secondIndex]
        #print('correct Word: ', correctWord)
        if guess in guessedWords:
                print("You've already guessed that. Try again.")
                guess = input("\nEnter a guess: ")
                result = checkGuess(guess,cg_wordToGuessAndIndex)
                printDisplay(displayList, wordSameLetters)
        else:
            for alist in wordSameLetters:
                for correctWord in alist:
                    if guess == correctWord :
                        print('Correct!')
                        addToGuessedWords(guess)
                        index = WordsIndex(correctWord, wordSameLetters)
                        #print(index)
                        wordToGuessAndIndex = []
                        wordList = []
                        wordList.append(correctWord)
                        wordToGuessAndIndex.append(wordList)
                        wordToGuessAndIndex.append(index)
                        #print('WTGAI: ', wordToGuessAndIndex)
                        updateDisplay(wordToGuessAndIndex)
                        
                #if guess == correctWord :
                    #print('Correct!')
                    #updateDisplay(cg_wordToGuessAndIndex)
            else:
                flattenedWordsSameStart = [item for sublist in wordSameLetters for item in sublist]
                lengthTotalWords = len(flattenedWordsSameStart)
                if len(guessedWords) != lengthTotalWords:
                    print("That guess is incorrect. Try Again.")
                    printDisplay(displayList, wordSameLetters)
                    guess = input("\nEnter a guess: ")
                    result = checkGuess(guess, wordToGuessAndIndex)
                        

def printDisplay(pd_displayList, pd_wordsSameStart):
    print('\n\n')
    #diplay random scrambled word
    #wordToGuessAndIndex = WordToGuess(pd_wordsSameStart)
    flattenedWordsSameStart = [item for sublist in wordSameLetters for item in sublist]
    lengthTotalWords = len(flattenedWordsSameStart)
    if len(guessedWords) == lengthTotalWords:
        print('Congrats you won!')
        return
    else:
        #wordToGuessAndIndex = WordToGuess(pd_wordsSameStart) # in the form [[word][index,index]]
        #wordToGuess = wordToGuessAndIndex[0][0]
        wordToGuess = WordToGuess(pd_wordsSameStart)
        scrambledWord = scrambleLettersInWord(wordToGuess)
        print(scrambledWord, ':')
        i = -1
        for aList in pd_displayList:
            i += 1
            print(aList)
        guess = input("\nEnter a guess: ")
        result = checkGuess(guess,wordToGuess)
        if result != None:
            print('result: ',result) #TODO: still hits here after hits win statement above
    
displayList = startDisplay(wordSameLetters)
printDisplay(displayList, wordSameLetters)