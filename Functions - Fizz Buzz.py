def fizz_buzz(num1):
    if num1%3 == 0 and num1%5 != 0:
        return "Fizz"
    elif num1%5 == 0 and num1%3 != 0:
        return "Buzz"
    elif num1%5 == 0 and num1%3 == 0:
        return "FizzBuzz"
    else:
        return num1
    
print(fizz_buzz(5))
print(fizz_buzz(3))
print(fizz_buzz(15))
print(fizz_buzz(18))
print(fizz_buzz(20))
print(fizz_buzz(66))
print(fizz_buzz(30))
