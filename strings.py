#Строки:
#1 Свяжите переменную с любой строкой, состоящей не менее чем из 8 символов.
#Извлеките из строки первый символ, затем последний, третий с начала и третий с
#конца. Измерьте длину вашей строки.
val_str = "Brave new world"
print(val_str[0])
print(val_str[-1])
print(val_str[2])
print(val_str[-3])
print(len(val_str))
#2 Присвойте произвольную строку длиной 10-15 символов переменной и извлеките из
#нее следующие срезы:
#●
#первые восемь символов
#●
#четыре символа из центра строки
#●
#символы с индексами кратными трем
#●
#переверните строку

val_str = "Душещипательный"
slice_str = int(len(val_str) / 2)
print(val_str[0:7:1])
print(val_str[slice_str - 2: slice_str + 2])
print(val_str[2:15:3])
print(val_str[-1:-16:-1])
#3 Есть строка: “my name is name”. Напечатайте ее, но вместо 2ого “name” вставьте
#ваше имя.
my_name = "my name is name"

print(my_name[:11] + "Farruh" + my_name[16:])
#4 Есть строка: test_tring = "Hello world!", необходимо
#●
#напечатать на каком месте находится буква w
#●
#кол-во букв l
#●
#Проверить начинается ли строка с подстроки: “Hello”
#●
#Проверить заканчивается ли строка подстрокой: “qwe”
test_string = "Hello world!"
print(test_string.find("w"))
print(test_string.count("l"))
print("Hello".istitle())
print("qwe".islower())