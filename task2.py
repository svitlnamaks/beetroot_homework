# Task 2
# Exclusive common numbers.
# Generate 2 lists with the length of 10 with random integers from 1 to 10,
# and make a third list containing the common integers between the 2 initial lists without any duplicates.
# onstraints: use only while loop and random module to generate numbers
import random as rd

list1 = list()
list2 = list()
list3 = list()
n = 0
while n < 10:
    numbers = rd.randint(0, 10)
    n = n + 1
    list1.append(numbers)
    list2.append(numbers)
print(list1, list2)
our_list = list1 + list2

for number in our_list:
    if number not in list3:
        list3.append(number)
        continue
    if number in list3:
        continue
print(list3)
