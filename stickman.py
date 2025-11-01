wordList = ["monkey", "ape", "dinosaur", "fish", "python", "turtle", "dish", "code", "fog", "track"]
import random
randomIndex = random.choice(wordList)
numOfGuesses = 0
letterGuess = ""
wordGuess = ""

print(randomIndex)
for numOfGuesses in range(5):
    letterGuess = input("guess a letter to the word: ")
    numOfGuesses += 1
    if(letterGuess in randomIndex):
        print("your guess is in the word")
    else:
        print("your guess isnt in the word")
        
wordGuess = input("guess a word: ")

if(wordGuess == randomIndex):
    print("the word was ", randomIndex, " and your guess was correct")
else:
    print("the word was ", randomIndex, " and your guess was incorrect")

