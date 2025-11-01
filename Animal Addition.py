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
question = input("What animal would you like to learn the baby name of?: ")

if(question in babyAnimals):
    print("The baby name of " + question + " is " + babyAnimals[question])
else:
    decision = input("Would you like to add an entry to the dictionary? Enter 'yes' or 'no': ")
    if decision == "yes":
        newBabyName = input("Enter the baby name of the animale you entered: ")
        babyAnimals.update({question : newBabyName})
        print("You added " + question + " and the baby name of " + question + " is " + newBabyName)
    else:
        print("ok have a good day:)")
