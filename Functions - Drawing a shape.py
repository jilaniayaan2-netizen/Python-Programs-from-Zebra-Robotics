import turtle
window = turtle.Screen()
marty = turtle.Turtle()

shape = int(input("What shape would you like to draw?\nEnter '1' for square\nEnter '2' for circle\nEnter '3' for triangle\n"))
shapeSize = int(input("What is the size of the shape(in px)?\n"))
shapeColor = input("What is the color of the shape?\n")

def drawSquare(color, size):
    for x in range(0,4):
        marty.forward(size)
        marty.left(90)

def drawCircle(color, size):
    marty.circle(size)

def drawTriangle(color, size):
    marty.forward(size)
    marty.left(135)
    marty.forward(size)
    marty.left(90)
    marty.forward(size)
    marty.right(225)
    marty.forward(size)

marty.color(color)
marty.fillcolor(color) 
marty.begin_fill() 
if(shape == 1):
    drawSquare(shapeColor, shapeSize)
elif(shape == 2):
    drawCircle(shapeColor, shapeSize)
else:
    drawTriangle(shapeColor, shapeSize)

marty.end_fill()
