# Task 1
# The greatest number
# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers
import random as rd

our_num = list()
n = 0
while n < 20:
    numbers = rd.randint(0, 1000)
    n = n+1
    our_num.append(numbers)
print(our_num)
print('Largest element in list is ',max(our_num))
