name = ["Mark", "Joe", "Aaron"]
x = 0

def greeter(name):
    return("Hello there " + name + ".\nHow are you doing today " + name + "?\nIt's nice to meet you " + name + ".\n")

for x in range(0, 3):
    print(greeter(name[x]))
