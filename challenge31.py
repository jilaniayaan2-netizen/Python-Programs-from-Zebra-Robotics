userString = input("enter a word that i will remove the vowls of: ")
vowls = ["a", "e", "i", "o", "u"]
x = 0
outputString = ""

while x < len(userString):
    if(userString[x] not in vowls):
        outputString += userString[x]
    x+=1
print(outputString)
