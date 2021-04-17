# Task 3

# A simple calculator.

# Create a function called make_operation, which takes in a simple arithmetic operator
# as a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’)
# and an arbitrary number of arguments (only numbers) as the second parameter.
# Then return the sum or product of all the numbers in the arbitrary parameter. For example:

# the call make_operation(‘+’, 7, 7, 2) should return 16
# the call make_operation(‘-’, 5, 5, -10, -20) should return 30
# the call make_operation(‘*’, 7, 6) should return 42
def make_operation(oper, *args) :
    arguments = [args]
    return_val = arguments.pop()
    for argument in arguments :
        if oper == '+':
            return_val += argument
        elif oper == '-' :
            return_val -= argument
        elif oper == '*' :
            return_val = argument
        else :
            raise NotImplementedError

    return return_val


def make_operation_by_aval(oper, *args) :
    arguments = [args]
    return_val = arguments.pop()
    for argument in arguments :
        return_val = eval(f'{return_val}{oper}{argument}')
        return return_val





    print(make_operation('+', 7, 7, 2))
    print(make_operation('-', 5, 5, -10, -20))
    print(make_operation('*', 7, 6))

    print(make_operation_by_aval('+', 7, 7, 2))
    print(make_operation_by_aval('-', 5, 5, -10, -20))
    print(make_operation_by_aval('*', 7, 6))
