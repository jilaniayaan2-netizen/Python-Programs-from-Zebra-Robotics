def stringToList(stringToSplit, reverseOrNot):
    printTheList = []
    if reverseOrNot == True:
        for x in range(len(stringToSplit) - 1,-1,-1):
            printTheList.append(stringToSplit[x])
        return printTheList
    else:
        for x in range(len(stringToSplit)):
            printTheList.append(stringToSplit[x])
        return printTheList
inputString = input("Enter a word to be converted into a list: ")
yesOrNo = bool(input("would you like to reverse the output? Enter True or False: "))
myNewList = stringToList(inputString, yesOrNo)
print(myNewList)
