# Task 1
# The Guessing Game.
# Write a program that generates a random number between 1 and 10
# and lets the user guess what number was generated.
# The result should be sent back to the user via a print statement.
import random

for i in range(0, 1):
    comp= random.randint(1, 10)

your_number = input('Lets paly a game . Enter your number :\n')
if your_number.isdigit() == False:
    print('Please enter correct input')
elif comp== int(your_number):
    print('Correct !')
else:
    print('Correct number have to be ' + str(comp))