# Условия
# 1
# Дано целое число. Если оно является положительным, то прибавить к нему 1; в
# противном случае не изменять его. Вывести полученное число.

def positive_number(num):
    """
    Checks given number is positive or negative and add 1 if it positive else return it
    """
    if num > 0:
        num += 1
    else:
        num += 0
    return num


print(positive_number(11))


# 2
# Даны три целых числа. Найти количество положительных чисел в исходном
# наборе.
def positive_counter(b):
    """
    Counts quantity of positive numbers in list and return of count of them
    :param b list:
    """
    counter = 0
    for i in b:
        if i > 0:
            counter += 1
    return counter


print(positive_counter([10, -12, -40]))


# 3
# Дан номер года (положительное целое число). Определить количество дней в
# этом году, учитывая, что обычный год насчитывает 365 дней, а високосный — 366
# дней. Високосным считается год, делящийся на 4, за исключением тех годов, которые
# делятся на 100 и не делятся на 400 (например, годы 300, 1300 и 1900 не являются
# високосными, а 1200 и 2000 являются).
def check_year(year):
    """
    Checks is year leap or not
    :param year int:
    """
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        year = 366
    else:
        year = 365
    return year


print(check_year(2020))


# 4
# Дано целое число в диапазоне 1–7. Вывести строку — название дня недели,
# соответствующее данному числу (1 — «понедельник», 2 — «втор- ник» и т. д.).
def days():
    """
    Returns days based on inputted digit
    """
    days_list = {1: "Понедельник", 2: "Вторник", 3: "Среда", 4: "Четверг", 5: "Пятница", 6: "Суббота", 7: "Воскресенье"}
    day = int(input("Введите порядковый номер дня: "))
    a = days_list.get(day, "Такого дня нет")
    return a


print(days())
# 5
# Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 —
# миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер. Дан номер единицы массы (целое
# число в диапазоне 1–5) и масса тела в этих единицах (вещественное число). Найти
# массу тела в килограммах.

def kg():
    """
    :return: Mass in kg
    """
    user_input = int(input("Введите номер чтобы рассчитать массу: "))
    match user_input:
        case 1:
             user_input = user_input
             return user_input
        case 2:
            user_input = user_input / 1000000
            return user_input
        case 3:
           user_input = user_input / 1000
           return user_input
        case 4:
             user_input = user_input * 1000
             return user_input
        case 5:
            user_input = user_input * 100
            return user_input
        case _:
            return "Ваш номер отсутствует в нашей системе метрик"

print(kg())