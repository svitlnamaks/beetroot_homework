#Task 3
#Words combination
#Create a program that reads an input string and then creates
# and prints 5 random strings from characters of the input string.
#For example, the program obtained the word ‘hello’,
# so it should print 5 random strings(words)
# that combine characters ‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …
#Tips: Use random module to get random char from string)

import random
word=('h','e','l','l','o')
n=5
while n>0 :
    n=n-1
    new_word=''.join(random.sample(word,5))
    print(new_word)