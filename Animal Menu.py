babyAnimals = {'hippo' : 'calf',
               'horse' : 'foal',
               'dog' : 'pup',
               'kangaroo' : 'joey',
               'monkey' : 'infant',
               'owl' : 'owlet',
               'parrot' : 'chick',
               'rabbit' : 'bunny',
               'rat' : 'pup',
               'cow' : 'calf',
               'skunk' : 'kit',
               'sheep' : 'lamb'}
menu = "0"

while menu != "4":
    menu = input("Select one of the options:\n1.Look up animal babies\n2.Add animal and baby\n3.Delete animal and baby\n4.Quit program\n")
    if(menu == "1"):
        question = input("What animal would you like to learn the baby name of?: ")
        print("The baby name of " + question + " is " + babyAnimals[question])
    elif(menu == "2"):
        question = input("Enter name of animal: ")
        newBabyName = input("Enter the baby name of the animal you entered: ")
        babyAnimals.update({question : newBabyName})
        print("You added " + question + " and the baby name of " + question + " is " + newBabyName)
    elif(menu == "3"):
        deleteAnimal = input("select animal and baby pair to delete from dictionary: ")
        babyAnimals.pop(deleteAnimal)
        print("You deleted " + deleteAnimal + " from the dictionary.")
        print(babyAnimals)

    
    
