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
    print("That animal is not on the list.")
