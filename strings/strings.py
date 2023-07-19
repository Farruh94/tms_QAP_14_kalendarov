# Строки:
# 1 Свяжите переменную с любой строкой, состоящей не менее чем из 8 символов.
# Извлеките из строки первый символ, затем последний, третий с начала и третий с
# конца. Измерьте длину вашей строки.
def val_str(my_str):
    """
    :param my_str:
    :return: 'first element of string, last element of string, third element of string, third element from end of
    string' and 'measures the length of a string'
    """
    return f"{my_str[0]}\n{my_str[-1]}\n{my_str[2]}\n{my_str[-3]}\n{(len(my_str))}"


print(val_str("Hello World"))


# 2 Присвойте произвольную строку длиной 10-15 символов переменной и извлеките из
# нее следующие срезы:
# ●
# первые восемь символов
# ●
# четыре символа из центра строки
# ●
# символы с индексами кратными трем
# ●
# переверните строку

def change_str(stroka):
    """
    :param stroka: на вход дается строка
    :return: 'первые восемь символов', 'четыре символа из центра строки','символы с индексами кратными трем'
    'переворачивает строку'

    """
    centre_of_str = (stroka[4])
    print(centre_of_str)
    return stroka[0:7:1], stroka[int(len(stroka)/2) - 2: int(len(stroka)/2) + 2], stroka[2:14:3], stroka[::-1]


print(change_str("Душещипательный"))


# 3 Есть строка: “my name is name”. Напечатайте ее, но вместо 2ого “name” вставьте
# ваше имя.
def my_name(name):
    """
    Replaces second 'name' in string to user's name
    """
    user_name = "Farruh"

    return f"{name[:11]}{user_name}{name[16:]}"


print(my_name("my name is name"))


# 4 Есть строка: test_string = "Hello world!", необходимо
# ●
# напечатать на каком месте находится буква w
# ●
# кол-во букв l
# ●
# Проверить начинается ли строка с подстроки: “Hello”
# ●
# Проверить заканчивается ли строка подстрокой: “qwe”


def string(test_string):
    """
    Печатает на каком месте находится буква w,
    считает кол-во букв l
    Проверяет, начинается ли строка с подстроки: “Hello”
    """
    return test_string.find('w'), test_string.count('l'), test_string[0:4].istitle(), \
        test_string.islower()


print(string("Hello world"))
# print(string("qwe"))
