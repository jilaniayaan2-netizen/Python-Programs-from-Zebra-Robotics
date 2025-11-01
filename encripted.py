userSentence = input("Input a sentence, use all lower case letters or space: ")
x = len(userSentence)
newOutput = ""

for x in range(x):

    if userSentence[x] == ' ':
        newOutput += ' '
    elif userSentence[x] == 'z':
        newOutput += 'a'
    else:
        asciiValue = ord(userSentence[x])
        asciiValue += 1
        newOutput += chr(asciiValue)

print(newOutput)
