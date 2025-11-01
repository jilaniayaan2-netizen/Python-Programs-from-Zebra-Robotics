travelDestination = ["Costa Rica", "Florida"]
helpPhone = int(input("enter 1 to add a destination or enter 2 to find a destination. "))
addDestination = " "
findDestination = " "

if(helpPhone == 1):
    addDestination = input("What destination would you like to add? ")
    travelDestination = ("Costa Rica", "Florida", addDestination)
    print("you added " + travelDestination[2] + " to your travel list.")
    
if(helpPhone == 2):
    findDestination = input("What destination would you like to find? ")
    if(findDestination in travelDestination):
        print(findDestination, " is in your travel list")
    else:
        print(findDestination, " isn't in your travel list")


