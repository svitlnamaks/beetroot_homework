#Task 2
#The birthday greeting program.
#Write a program that takes your name as input, and then your age as input and greets you with the following:
#“Hello <name>, on your next birthday you’ll be <age+1> years”
my_name=input('What is you name ?\n')
my_age=input('Hove old are you ?\n')
age=int(my_age)+1
print('Hello %s,on your next birthday you’ll be %s years '% (my_name, age))