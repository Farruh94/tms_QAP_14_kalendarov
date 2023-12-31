# Цикл for
# 1
# Даны два целых числа A и B (A < B). Найти сумму всех целых чисел от A до B
# включительно.
a = 10
b = 20
c = 0
for i in range(a, b + 1):
    c += i
print(c)

# 2
# Найти сумму всех натуральных чисел от A до B
digit_1 = 1
digit_2 = 20
for natural_int_1 in (digit_1, digit_2):
    if natural_int_1 % natural_int_1 == 0 and natural_int_1 % 1 ==0:
        natural_int_1 += natural_int_1
print(natural_int_1)
# Не очень понял, эти два задания.
# 3
# Найти произведение положительных, сумму и количество отрицательных
# из 10 введенных целых значений.
user_int = [10, 11, 15, -20, -3, 5, 7, -6, 33, 25]
positive_int_product = 1
negative_int_counter = 0
negative_int_summ = 0

for i in user_int:
    if i >= 0:
        positive_int_product = positive_int_product * i
    elif i < 0:
        negative_int_counter += 1
        negative_int_summ += i

print(positive_int_product)
print(negative_int_counter)
print(negative_int_summ)

# 4
# Дан словарь пловцов с их результатами. Напечатать лучший результат
# заплыва среди 6 участников.
# Бекиш Александр - 21,07
# Будник Алексей - 20,34
# Гребень Анастасия - 22,12
# Давидович Татьяна - 30
# Дешук Дмитрий - 24.01
# Казак Анна - 28,17
swimmers = {"Бекиш Александр": 21.07, "Будник Алексей": 20.34, "Гребень Анастасия": 22.12, "Давидович Татьяна": 30,
            "Дешук Дмитрий": 24.01, "Казак Анна": 28.17}
print(min(swimmers, key=swimmers.get))
# 5
# Есть массив чисел. Известно, что каждое число в этом массиве имеет пару,
# кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5 Напишите программу, которая будет выводить
# уникальное число
#
list_1 = [1, 2, 3, 3, 1, 2, 4, 3, 7]
unique_elem = []
for i in list_1:
    if list_1.count(i) < 2:
        unique_elem.append(i)
print(unique_elem)

# Цикл while
# 1
# Дано число N. Найти произведение всех чисел от 0 до N.
number = 10
start = 0
positive_int = 1
while start < number:

    positive_int *= start
    start += 1
print(positive_int)

# 2
# Поле засеяли цветами двух сортов на площади S1 и S2. Каждый год
# площадь цветов первого сорта увеличивается вдвое, а площадь второго сорта
# увеличивается втрое. Через сколько лет площадь первых сортов будет
# составлять меньше 10% от площади вторых сортов.
field_s_1 = 10
field_s_2 = 2
year = 0
while field_s_1 > field_s_2 * 0.1:
    year += 1
    field_s_1 *= 2
    field_s_2 *= 3
print("Площадь цветов первого сорта: ", field_s_1)
print("Площадь цветов второго сорта: ", field_s_2)
if 4 >= year % 10 <= 4 and year % 10 != 0:
    print("Через", year, "года площадь цветов первого сорта будет меньше 10% от площади цветов второго сорта.")
elif 4 < year <= 20:
    print("Через", year, "лет площадь цветов первого сорта будет меньше 10% от площади цветов второго сорта.")
# 3
# Дано целое число N (>0). Используя операции деления нацело и взятия
# остатка от деления, найти количество и сумму его цифр.

number_1 = int(input("Введите целое число: "))
sum_of_number = 0
count = 0
the_last = number_1 % 10
while number_1 != 0:
    last_digit = number_1 % 10
    sum_of_number += last_digit
    count += 1
    number_1 = number_1 // 10

print("Сумма введенных цифр: ", sum_of_number)
print("Количество цифр: ", count)

# 4
# Деду M лет, а внуку N лет. Через сколько лет дед станет вдвое старше
# внука. И сколько при этом лет будет деду и внуку.
grand_pa = 50
grand_s = 2
year_1 = 0
while grand_pa > grand_s * 2:
    year_1 += 1
    grand_pa += 1
    grand_s += 1
print("Возраст дедушки ", grand_pa)
print("Возраст внука ", grand_s)
if 4 >= year_1 % 10 <= 4 and year_1 % 10 != 0:
    print("Через", year_1, "года возраст внука будет вдвое меньше возраста дедушки.")
elif 4 < year_1 <= 20 or year_1 % 10 > 0:
    print("Через", year_1, "лет возраст внука будет вдвое меньше возраста дедушки.")
