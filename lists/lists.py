# Списки:
# 1 Создайте два любых списка и свяжите их с переменными.
# 2 Извлеките из первого списка второй элемент.

list_1 = [0, 1, 2, 3, 4]
list_2 = [5, 6, 7, 8, 9]

def work_on_lists():
    """
    Returns 2nd elem of first list
    """
    return list_1[1]


print(work_on_lists())


# 3 Измените во втором списке последний элемент. Выведите список на экран.
def change_value():
    """
    Change last elem of second list
    """
    list_2[-1] = 10
    return list_2

print(change_value())

# 4 Соедините оба списка в один, присвоив результат новой переменной. Выведите
# получившийся список на экран.

def merge_lists():
    """
    Merge lists
    """
    global list_3
    list_3 = list_1 + list_2
    return list_3


print(merge_lists())
# 5 "Снимите" срез из соединенного списка так, чтобы туда попали некоторые части
# обоих первых списков. Срез свяжите с очередной новой переменной. Выведите
# значение этой переменной.
def list_elems():
    """
    Returns elems of merged list
    """
    return list_3[3:7]

print(list_elems())


# 6 Добавьте в список два новых элемента и снова выведите его.
def add_elems():
    """
    Add 2 elems to merged list
    """
    list_3.append(11)
    list_3.append(14)
    return list_3


print(add_elems())

# 7 Даны списки:
# Нужно вернуть список, который состоит из элементов, общих для этих двух`
# списков. -- !не использовать циклы
def merged_list():
    """
    Returns unique elems from 2 lists
    """
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = set(a + b)
    return list(c)


print(merged_list())

# 8 Есть список: [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3] оставить в нем только уникальные
# значения. !не использовать циклы

def unique_list(*args):
    """
    Returns unique elems of list
    """
    unique_list_1 = set(args)
    return list(unique_list_1)


print(unique_list(1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3))
