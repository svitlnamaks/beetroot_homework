# Task 1
# Make a program that has some sentence (a string) on input and returns a dict containing
# all unique words as keys and the number of occurrences as values.
import re


# String-> List-> Dictionary
# якщо не перевести строку в список то в словнику будьть окремі букви а не слова

def convert1(string):  # Функція для переведеня рядка в лист
    li = list(string.split(" "))
    return li


# мій рядок
my_message = 'I never need anybody\'s in any way, but now these these days are gone, i\'m not so self assured ' \
             '(I never need anybody\'s in any way) (I never need anybody\'s in any way)'

new_message = re.sub(r'[^\w\s]', '', my_message)  # використовуємо модуль rе для того щоб прибрати розділові знаки

my_list = convert1(new_message)
my_dict = dict()  # створюємо наш словник

for word in my_list:
    my_dict[word] = my_dict.get(word, 0) + 1  # не вдається вирішити проблему з апосстрофом
print(my_dict)
