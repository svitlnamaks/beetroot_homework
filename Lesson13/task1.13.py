# Task 1

# Write a Python program to detect the number of local variables declared in a function.

def abc():
    x = 18
    y = 2.5
    str1 = 'ababalamaha'
    c = ['juice', 'tea', 'coffee']


if __name__ == '__main__':
    print(f'We have {abc.__code__.co_nlocals} variables in our function')
