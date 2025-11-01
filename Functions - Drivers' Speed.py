def driverSpeed(speed, points):
    if(speed <= 70 ):
        return "ok"
    elif(speed > 70):
        points = (speed - 70)/5
        return "you have " + str(points) + " points. " + str(12 - points) + " more points and your license will be suspended."
    elif(points == 12):
        return "License suspended"

speed = int(input("enter your speed: "))
points = 0
print(driverSpeed(speed, points))
    
