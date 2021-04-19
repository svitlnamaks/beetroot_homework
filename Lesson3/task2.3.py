# Task 2
# The valid phone number program.
# Make a program that checks if a string is in the right format for a phone number.
# The program should check that the string contains
# only numerical characters and is only 10 characters long.
# Print a suitable message depending on the outcome of the string evaluation.


phone_number = input('Please enter your  number :\t')
# phone_number2=phone_number.split(' ')
# phone_number3=phone_number2.replace('')

if phone_number.isdigit() == False:
    print('Please enter correct phone number please.\nPhone number can not contain letters')
if len(phone_number) != 10:
    if len(phone_number) < 10:
        print('Your phone number is too short .Please try again.')
    elif len(phone_number) > 10:
        print('Your phone number is too long. Please try agin. ')

elif phone_number.isdigit() == True and len(phone_number) == 10:
    print('Thank you !We will call you back ASAP')