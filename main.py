import time
from datetime import date
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


def add(a):
    def inner(b):
        return a + b
    time.time()
    return inner

calc = add(11)
print(calc(12))





class File:
    def init(self, content, date, size):
        self.content = content
        self.date = date
        self.size = size

    def eq(self, other):
        """

        :param other:
        :return:
        """
        return self.content == other.content and self.size == other.size

    def add(self, other):
        return File(self.content + other.content, date.today(), self.size + other.size)

    def str(self):
        return f"{self.content}, {self.date}, {self.size}"


file_1 = File("something", "15.07.2023", 8)
file_2 = File("something", "15.07.2023", 8)
file_3 = File("something", "15.07.2023", 8)

print(file_1 == file_2 == file_3)
print(id(file_1))
print(id(file_2))
print(id(file_3))
file_4 = file_1 + file_2
print(file_4)
print(file_4.content)
print(file_4.date)
print(file_4.size)