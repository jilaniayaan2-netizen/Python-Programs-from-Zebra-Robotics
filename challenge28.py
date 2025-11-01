groceryList = ["milk", "eggs"]
groceryManeger = int(input("enter 1 to add an item to your gocery list, enter 2 to print your grocery list, enter 3 to sort your grocery list, enter 4 to remove grocery list, enter 5 to count groceries, and enter 6 to rplace an item. "))

addItem = " "
removeItem = " "
replaceItem = " "
newItem = " "

if(groceryManeger == 1):
    addItem = input("what item would you like to add to your list? ")
    groceryList = ("eggs", "milk", addItem)
    print("you added " + groceryList[2] + " to your grocery list.")

if(groceryManeger == 2):
    print(groceryList)
    
if(groceryManeger == 3):
    groceryList.sort()
    print(groceryList)
    
if(groceryManeger == 4):
    removeItem = input("What item would you like to remove? ")
    if(removeItem in groceryList):
        groceryList.remove(removeItem)
        print("you removed " + removeItem + " from your list.")
    else:
        print("Item is not in list, so it can't be removed.")
        
if(groceryManeger == 5):
    print(len(groceryList5))
    
if(groceryManeger == 6):
    replaceItem = input("What item would you like to replace? ")
    if(replaceItem in groceryList):
        newItem = input("what would you like to replace it with? ")
        index = groceryList.index(replaceItem)
        groceryList.insert(index, newItem)
        print("you replaced " + replaceItem + " with " + newItem + ".")
    else:
        print("we cannot replace that item because it isn't in the list.")
    

