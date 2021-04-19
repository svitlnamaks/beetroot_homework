number1 = input('Enter first number:')
number2 = input('Enter second number:')
action = input('Enter action :')
try:
    n1 = float(number1)
    n2 = float(number2)
    # Addition
    if action == '+':
        print(n1 + n2)
    # Subtraction
    elif action == '-':
        print(n1 - n2)
    # Division
    elif action == '/':
        print(n1 / n2)
        # Multiplication
    elif action == '*':
        print(n1 * n2)
        # Exponent(Power)
    elif action == '%':
        print(n1 % n2)
        # Modulus
    elif action == '**':
        print(n1 ** n2)
        # Floor division
    else:
        print(n1 // n2)

except:
    print('Please enter correct input ')
