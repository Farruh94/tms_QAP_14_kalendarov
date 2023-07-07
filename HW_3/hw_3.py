# 1 Привести к целому типу -1.6, 2.99

float_to_int = -1.6
float_to_int_1 = 2.99
print(int(float_to_int))
print(int(float_to_int_1))

print("==============================")

#1.2 Определить переменные всех типов и выведете их на экран
val = "rtt"
print(type(val))
val = 145
print(type(val))
val = [1, 2, 4]
print(type(val))
val = {1, 2, 3}
print(type(val))
val = (1, 2, None)
print(type(val))
val = {"val": 12, "val2": "34"}
print(type(val))
#1.3 Найти значение выражений

x = 17 / 2 * 3 + 2
print(x)
x1 = 2 + 17 / 2 * 3
print(x1)
x2 = 19 % 4 + 15 / 2 * 3
print(x2)
x3 = (15 + 6) - 10 * 4
print(x3)
x = 17 / 2 % 2 * 3**3
print(x3)
print("==============================")
# 2 Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
my_str = "www.my_site.com#about"
print(my_str.replace("#", "/"))

print("==============================")

# 3 Напишите программу, которая добавляет ‘ing’ к слову ‘stroka’

str_1 = "stroka"
str_2 = "ing"
print(str_1+str_2)

print("==============================")

# 4 В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
fio = "Kalendarov Farruh"
fio_1 = fio.split()
print(fio_1[-1], fio_1[0])


# 5 Напишите программу которая удаляет пробел в начале, в конце строки
my_space = " Hello World! "
print(my_space.strip(" "))

print("==============================")

# 6 Создайте словарь, связав его с переменной school, и наполните его
# данными которые бы отражали количество учащихся в десяти разных классах (например, 1а, 1б, 2б, 6а, 7в и т.д.).
school = {"1a": 20, "1б": 21, "2а": 31, "2в": 29, "3а": 25, "3б": 29, "4а": 30, "5а": 28,
          "6б": 30, "7в": 31, "8а": 29, "9а": 28, "10б": 28, "11а": 29}
print(school)

print("==============================")
# 7 Создайте список и извлеките из него списка второй элемент.
list_1 = ["w", "o", "n", "d", "e", "r", "f", "u", "l", "l"]
print(list_1[1])
print("==============================")

# 8 Вывести входит ли строка1 в строку2 (пример: employ и employment)
string_1 = "employ"
string_2 = "employment"

print(string_1 in string_2)

print("==============================")
# 9 Вывести нужные символы

# x = "My name is Agent Smith"

# print(x[?]) #y

# print(x[?:?:?]) #nesgt

agent = "My name is Agent Smith"

print(agent[1])
print(agent[3:16:3])
print("==============================")
# 10* Есть массив чисел. Известно, что каждое число в этом массиве имеет пару,
# кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5


numbers = [1, 5, 2, 9, 2, 9, 1]
def foo(numbers):
    return [i for i in numbers if numbers.count(i) < 2]

print(foo(numbers))

# Напишите программу, которая будет выводить уникальное число

#PS: создать ПР, использовать git (через терминал), если кто-то уже работал с
# функциями использовать их при написании дз

