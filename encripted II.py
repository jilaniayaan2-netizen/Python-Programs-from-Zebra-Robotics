userSentence = input("Input a sentence, use all lower case letters or space: ")
numOfShifted = int(input("Input how many charecters each charecter should be shifted by(1 - 25): "))
x = len(userSentence)
asciiValue = 0
newOutput = ""

for x in range(x):
    asciiValue = ord(userSentence[x])
    
    if userSentence[x] == ' ':
        newOutput += ' '
    elif (asciiValue + numOfShifted) > ord("z"):
        asciiValue = (asciiValue + numOfShifted) - 26
        newOutput += chr(asciiValue)
    else: 
        asciiValue += numOfShifted
        newOutput += chr(asciiValue)

print(newOutput)
