# Task 1
# String manipulation
# Write a Python program to get a string made of the first 2 and the last 2 chars
# from a given string. If the string length is less than 2, return instead of the empty string.
# Sample String: 'helloworld'
# Expected Result : 'held'
# Sample String: 'my'
# #Expected Result : 'mymy'
# Sample String: ' x'
# Expected Result: Empty String
# Tips:
# Use built-in function len() on an input string
# Use positive indexing to get the first characters of a s
# tring and negative indexing to get the last characters

my_words = input('Enter your input please :\n')
if len(my_words) >= 2:
# I can't find the reason why following line doesn't work  print(my_words[-2:2])
    a1 = my_words[:2]
    a2 = my_words[-2:]
    print(a2+a1)
else:
    print('Empty String')
