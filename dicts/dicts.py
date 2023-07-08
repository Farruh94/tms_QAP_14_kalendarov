#Словари:
#1 Создайте словарь, связав его с переменной school, и наполните его данными,
#которые бы отражали количество учащихся в десяти разных классах (например, 1а, 1б,
#2б, 6а, 7в и т.д.).
school = {'1а': 20, "1б": 21, "2а": 31, "2в": 29, "3а": 25, "3б": 29, "4а": 30, "5а": 28,
          "6б": 30, "7в": 31, "8а": 29, "9а": 28, "10б": 28, "11а": 29}

#2 Узнайте сколько человек в каком-нибудь классе.
def some_value():
    """
    Returns some class
    """
    return school['10б']

print(some_value())
#3 Представьте, что в школе произошли изменения, внесите их в словарь:
#◦ в трех классах изменилось количество учащихся;

def change_class():
    """
    Change classes
    """
    school["1а"]=25
    school["4а"]=26
    school["9а"]=31
    return school

print(change_class())
#◦ в школе появилось два новых класса;
def add_classes():
    """
    Add classes
    """
    school["7а"]=30
    school["10а"]=26
    return school

print(add_classes())
#◦ в школе расформировали один из классов.

def remove_class():
    """
    Remove classes
    """
    school.pop("5а")
    return school

print(remove_class())
#4 Выведите содержимое словаря на экран.

def school_1():
    """
    Returns all classes
    """
    return school

print(school_1())
