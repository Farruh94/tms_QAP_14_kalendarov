# Цикл for
# 1
# Даны два целых числа A и B (A < B). Найти сумму всех целых чисел от A до B
# включительно.
def int_number(a, b, c=0):
    """
    Summ of whole digits in range
    :param a: int
    :param b: int
    :param c: int
    """
    for num in range(a, b + 1):
        c = c + num
    return c


print(int_number(1, 10))


# 2
# Найти сумму всех натуральных чисел от A до B

def natural_num(digit_1, digit_2):
    """
    sum of natural digits in range
    :param digit_1: int    :param digit_2:
    """
    for natural_int_1 in (digit_1, digit_2):
        if natural_int_1 % natural_int_1 == 0 and natural_int_1 % 1 == 0:
            natural_int_1 += natural_int_1
    return natural_int_1


print(natural_num(1, 20))


# 3
# Найти произведение положительных, сумму и количество отрицательных
# из 10 введенных целых значений.


def negative_counter(*args):
    """
    Count of negative digits in list
    """

    positive_int_product = 1
    negative_int_counter = 0
    negative_int_summ = 0
    for i in args:
        if i >= 0:
            positive_int_product = positive_int_product * i
        elif i < 0:
            negative_int_counter += 1
            negative_int_summ += i
    return f"Произведение положительных чисел равна {positive_int_product}\nКоличество отрицательных чисел" \
           f" {negative_int_counter}\nСумма отрицательных чисел{negative_int_summ}"


print(negative_counter(10, 11, 15, -20, -3, 5, 7, -6, 33, 25))


# 4
# Дан словарь пловцов с их результатами. Напечатать лучший результат
# заплыва среди 6 участников.
# Бекиш Александр - 21,07
# Будник Алексей - 20,34
# Гребень Анастасия - 22,12
# Давидович Татьяна - 30
# Дешук Дмитрий - 24.01
# Казак Анна - 28,17
def the_best_swimmer():
    """
    :return: The best result of swimmers
    """
    swimmers = {"Бекиш Александр": 21.07, "Будник Алексей": 20.34, "Гребень Анастасия": 22.12, "Давидович Татьяна": 30,
                "Дешук Дмитрий": 24.01, "Казак Анна": 28.17}
    return min(swimmers, key=swimmers.get)


print(the_best_swimmer())
# 5
# Есть массив чисел. Известно, что каждое число в этом массиве имеет пару,
# кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5 Напишите программу, которая будет выводить
# уникальное число
#

def unique_number(*args):
    """
    :return: Unique digit in list
    """
    return [i for i in args if args.count(i) < 2]


print(unique_number(1, 2, 3, 3, 1, 2, 4, 3))


# Цикл while
# 1
# Дано число N. Найти произведение всех чисел от 0 до N.

def pow_digits(end):
    """
    Power of all digits in range
    """
    positive_int = 1
    start = 0
    while start < end:
        positive_int *= start
        start += 1
    return positive_int

print(pow_digits(15))

# 2
# Поле засеяли цветами двух сортов на площади S1 и S2. Каждый год
# площадь цветов первого сорта увеличивается вдвое, а площадь второго сорта
# увеличивается втрое. Через сколько лет площадь первых сортов будет
# составлять меньше 10% от площади вторых сортов.

def field_square_per_year(field_s_1, field_s_2, year=0):
    """
    In how many years will the area of the first varieties be less than 10% of the area of the second varieties.
   """
    while field_s_1 > field_s_2 * 0.1:
        year += 1
        field_s_1 *= 2
        field_s_2 *= 3
    print(f"Площадь цветов первого сорта, {field_s_1}\nПлощадь цветов второго сорта, {field_s_2}")
    if 4 >= year % 10 <= 4 and year % 10 != 0:
       return f"Через {year} года площадь цветов первого сорта будет меньше 10% от площади цветов " \
               f"второго сорта."
    else:
        return f"Через {year} лет площадь цветов первого сорта будет меньше 10% от площади цветов " \
               "второго сорта."

print(field_square_per_year(10, 15))
# 3
# Дано целое число N (>0). Используя операции деления нацело и взятия
# остатка от деления, найти количество и сумму его цифр.
def work_on_numbers(sum_of_number=0, count=0):
    """
    Sum and quantity of digits in number
    """
    number_1 = int(input("Введите целое число: "))
    the_last = number_1 % 10
    while number_1 != 0:
        last_digit = number_1 % 10
        sum_of_number += last_digit
        count += 1
        number_1 = number_1 // 10
    return f"Сумма введенных цифр: {sum_of_number}\nКоличество цифр: {count}"

print(work_on_numbers())

# 4
# Деду M лет, а внуку N лет. Через сколько лет дед станет вдвое старше
# внука. И сколько при этом лет будет деду и внуку.
def grandpa_and_grand_s_age(grand_pa, grand_s, year_1=0):
    """
    Count when grandson will be 2x younger than grandfather
    """
    while grand_pa > grand_s * 2:
        year_1 += 1
        grand_pa += 1
        grand_s += 1
    print("Возраст дедушки ", grand_pa)
    print("Возраст внука ", grand_s)
    if 4 >= year_1 % 10 <= 4 and year_1 % 10 != 0:
        return f"Через {year_1} года возраст внука будет вдвое меньше возраста дедушки."
    elif 4 < year_1 <= 20 or year_1 % 10 > 0:
        return f"Через {year_1} лет возраст внука будет вдвое меньше возраста дедушки."

print(grandpa_and_grand_s_age(50, 3))

