# Task 3
# List comprehension exercise
# Use a list comprehension to make a list containing tuples (i, j) where `i` goes from 1 to 10
# and `j` is corresponding to `i` squared.
my_list = list(range(1, 11))
my_list2 = [(i, i ** 2) for i in my_list]
print(my_list2)