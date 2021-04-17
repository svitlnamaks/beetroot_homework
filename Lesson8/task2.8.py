# Task 2
# Write a function that takes in two numbers from the user via input(),
# call the numbers a and b, and then returns the value of squared a divided by b,
# construct a try-except block which raises an exception
# if the two values given by the input function were not numbers,
# and if value b was zero (cannot divide by zero).

def divide() :
    a = input('Enter first number:\n')
    b = input('Enter second number:\n')
    try :
        c = print(float(a) ** 2 / float(b))
        return c
    except :
        if a.isdigit() != True or b.isdigit() != True :
            raise TypeError
        else :
            raise ZeroDivisionError


divide()
