# Task 3
# Extracting numbers.
# Make a list that contains all integers from 1 to 100,
# then find all integers from the list that are divisible by 7 but not a multiple of 5,
# and store them in a separate list. Finally, print the list.
a=list(range(1,101))
b=list()
i=0
while i<len(a):
    if i%5!=0 and i%7==0:
        b.append(i)
    i=i+7
print(b)
