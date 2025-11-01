n = int(input("input a number "))
x = 0

while n >= 0:
    x += n
    n -= 1
    if n == 0:
        print("the sum of all the numbers is", x)
