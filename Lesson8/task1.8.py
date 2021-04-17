# Task 1
# Write a function called oops that explicitly raises an IndexError exception when called.
# Then write another function that calls oops inside a try/except statement to catch the error.
# What happens if you change oops to raise KeyError instead of IndexError?

# створюємо функцію
def oops() :
    raise IndexError


# oops()
def new_fun() :
    my_list = [1, 2, 3, 4, 5]
    try :
        oops()
    except KeyError :  # IndexError :
        print('IndexError')


new_fun()

# Коли виконується "except  IndexError" на екран виводиться print('IndexError')(тобто наша функція відловлює помилку ).
# Але коли ми except KeyError то наша  фукція більше не відловлює нашу помилку тому наша програма не працює правильним чином.
