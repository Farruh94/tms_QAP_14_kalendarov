# Логические операции:
# 1 Присвойте двум переменным любые числовые значения.
age_1 = 25
age_2 = 78
# 2 Составьте четыре сложных логических выражения с помощью оператора and, два из
# которых должны давать истину, а два других - ложь.

print(age_1 > 21 and age_2 == 78)
print(age_1 == 25 and age_2 > 77)
print(age_1 < 25 and age_2 == 78)
print(age_1 > 25 and age_2 > 78)
print("==========================")
# 3 Аналогично выполните п. 2, но уже используя оператор or.
print(age_1 > 21 or age_2 == 78)
print(age_1 == 25 or age_2 > 77)
print(age_1 < 25 or age_2 < 78)
print(age_1 > 25 or age_2 > 78)
print("==========================")
# 4 Попробуйте использовать в сложных логических выражениях работу с переменными
# строкового типа.

name = "Ivan"
surname = "Petrov"
print(name in surname and name is surname)
print(name.islower() and surname.islower())
print(len(name) < len(surname) and name.istitle() and surname.istitle())

print("==========================")
print(name in surname or name is surname)
print(name.islower() or surname.isdigit())
print(len(name) < len(surname) or name.istitle() or surname.istitle())

