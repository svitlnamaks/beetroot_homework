import math as mt

value = [25.6, 38.4]
# Математичну дію
total = mt.fsum(value)
# Запитуємо користувача про введеня даних ( відповідь на питання )
user = input('What is the sum of 25.6 and 38.4? You have 3 attempt\n')
# Порівнюємо відповідь користувача з результатом
try:
    user1 = float(user)
    count = 4
    while count > 0 and user.isdigit() is True:
        count = count - 1
        if user1 != total:
            print('Sorry your answer is not correct =(Try again')
            user = input('What is the sum of 25.6 and 38.4? You have 3 attempt\n')
            user1 = float(user)
            if total == user1:
                print('Great job !')
                break
            if count == 1:
                print('You used all your attempts')

        if total == user1:
            print('Great job !')
            break
except:
    print('Sorry you entered wrong input')