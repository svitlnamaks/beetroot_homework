# Task 3
# The name check.
# Write a program that has a variable with your name stored (in lowercase)
# and then asks for your name as input.
# The program should check if your input is equal to the stored name
# even if the given name has another case, e.g.,
# if your input is “Anton” and the stored name is “anton”, it should return True.

my_name = 'Svitlana'
new_name = input('Please enter your name:\n')
n_name = new_name.capitalize()
count = 5
while n_name != my_name or count > 0:
    if n_name == my_name:
        print('Correct!')
        break
    if n_name != my_name:
        count = count - 1
        print('Please try again.\nYou have ' + str(count) + ' more attempts')
        new_name = input('Please enter your name:\n')
        n_name = new_name.capitalize()
    if count <= 0:
        print('You used all attempts')
        break