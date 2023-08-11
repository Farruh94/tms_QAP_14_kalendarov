import time
import datetime
name = "John Snow"
age = 29
print(name)


# def fibonacci(n):
#    if n == 0:
#        return 1
#    elif n == 1:
#        return 2
#    else:
#       return fibonacci(n - 2) + fibonacci(n - 1)
#
# print(fibonacci(2))
#
# def logging(level):
#     world = 'LOGGING'
#
#     def inner(url):
#         print(f"{world}: [{level}] - {url}")
#
#     return inner
#
# log_error = logging('ERROR')
# log_info = logging('INFO')
# log_war = logging('WARNINGS')
#
# url = 'https://github.com/8'
# url2 = 'https://github.com/0'
#
# log_error(url)
# log_war(url2)
# log_info(url2)

# def counter():
#     n = 0
#     def inner():
#         nonlocal n
#         n += 1
#         return n
#     return inner
#
# b = counter()
# print(b())
# print(b())
# print(b())
# print(b())


# def add(a):
#     def inner(b):
#         return a + b
#     time.time()
#     return inner
#
# calc = add(11)
# print(calc(12))
# calc = add(11)
# print(calc(12))
#
# class File:
#     def init(self, content, date, size):
#         self.content = content
#         self.date = date
#         self.size = size
#
#     def eq(self, other):
#         """
#
#         :param other:
#         :return:
#         """
#         return self.content == other.content and self.size == other.size
#
#     def add(self, other):
#         return File(self.content + other.content, date.today(), self.size + other.size)
#
#     def str(self):
#         return f"{self.content}, {self.date}, {self.size}"
#
#
# file_1 = File("something", "15.07.2023", 8)
# file_2 = File("something", "15.07.2023", 8)
# file_3 = File("something", "15.07.2023", 8)
#
# print(file_1 == file_2 == file_3)
# print(id(file_1))
# print(id(file_2))
# print(id(file_3))
# file_4 = file_1 + file_2
# print(file_4)
# print(file_4.content)
# print(file_4.date)
# print(file_4.size)


class Hero:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print("I am", self.name)

    def help(self, name):
        print(f"I am {self.name}! I will save you {name}")


spiderman = Hero("Spiderman", 19)
print(spiderman.name)
print(spiderman.age)
spiderman.help("Yura")


class Human:
    species = "Homo sapiens"

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    @staticmethod
    def speak(text):
        print(f"{text}")

    def print_name(self):
        print(self.name)

    def grew_up(self):
        self.age + 1

    def change_weight(self, kg):
        self.weight = kg

    def info(self):
        print(f"Name = {self.name}: age = {self.age}, weight = {self.weight}")

    @classmethod
    def print_species(cls):
        print(cls.species)


human_1 = Human("Adam", 0, 3)
human_1.print_species()
human_1.print_name()
human_1.grew_up()
human_1.grew_up()
human_1.grew_up()
human_1.grew_up()
human_1.grew_up()
human_1.grew_up()
human_1.grew_up()
human_1.grew_up()

human_1.change_weight(70)

human_1.speak("Hello")

human_1.info()
print("\n\n\n")

human_2 = Human("Eva", 0, 2.5)
human_2.print_species()
human_2.print_name()
human_2.grew_up()
human_2.grew_up()
human_2.grew_up()
human_2.grew_up()
human_2.grew_up()
human_2.grew_up()
human_2.grew_up()
human_2.grew_up()

human_2.change_weight(45)

human_2.speak("Hello, Adam")

human_2.info()


class Employee(Human):

    def __init__(self, company, experience, salary, name, age, weight=None):
        super().__init__(name, age, weight)
        self.company = company
        self.experience = experience
        self.salary = salary

    def company_name(self):
        print(self.company)

    def raise_salary(self):
        self.salary *= 1.5

    def raise_experience(self):
        self.experience += 1

    def employee_info(self):
        print(f"Works for {self.company}, {self.experience} years. For salary {self.salary}")


employee_1 = Employee("Kamaz", 2, 10000, "Egor", 20)
employee_1.employee_info()
employee_1.raise_salary()
employee_1.raise_experience()
employee_1.raise_salary()
employee_1.raise_experience()
print()
employee_1.employee_info()

employee_2 = Employee("Kamaz", 2, 10000, "Egor", 20)
employee_2.employee_info()
employee_2.raise_salary()
employee_2.change_weight(75)
employee_2.info()
employee_2.grew_up()
employee_2.print_name()
employee_2.employee_info()
employee_2.raise_salary()
employee_2.grew_up()
employee_2.print_name()
employee_2.employee_info()

# class File:
#     def init(self, content, date, size):
#         self.content = content
#         self.date = date
#         self.size = size
#
#     def eq(self, other):
#         """
#
#         :param other:
#         :return:
#         """
#         return self.content == other.content and self.size == other.size
#
#     def add(self, other):
#         return File(self.content + other.content, datetime.today(), self.size + other.size)
#
#     def str(self):
#         return f"{self.content}, {self.date}, {self.size}"
#
#
# file_1 = File("something", "15.07.2023", 8)
# file_2 = File("something", "15.07.2023", 8)
# file_3 = File("something", "15.07.2023", 8)
#
# print(file_1 == file_2 == file_3)
# print(id(file_1))
# print(id(file_2))
# print(id(file_3))
# file_4 = file_1 + file_2
# print(file_4)
# print(file_4.content)
# print(file_4.date)
# print(file_4.size)
