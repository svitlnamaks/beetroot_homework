# Task 3
# Extracting numbers.
# Make a list that contains all integers from 1 to 100,
# then find all integers from the list that are divisible by 7 but not a multiple of 5,
# and store them in a separate list. Finally, print the list.
new_list1 = list(range(1, 101))
num = 7
new_list2 = [i / num for i in new_list1]
new_list3 = new_list2[6:-3:7]
del new_list3[4:5]
del new_list3[8:9]
print(new_list3)
