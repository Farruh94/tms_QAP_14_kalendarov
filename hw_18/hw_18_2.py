# 4 Даны два файла произвольного типа. Поменять местами их
# содержимое. Файлы должны быть бинарного типа
import os

BASE_DIR = os.path.abspath(os.getcwd())
FILE_1 = os.path.abspath(os.path.join(BASE_DIR, './hw_18/files_2/first.bin'))
FILE_2 = os.path.abspath(os.path.join(BASE_DIR, './hw_18/files_2/second.bin'))


def read_file(name_1, name_2):
    with open(name_1, "rb") as file_1:
        file_1.read()
    with open(name_2, "rb") as file_2:
        file_2.read()


def first_file() -> str:
    with open(FILE_1, "rb") as first:
        first_file_content = first.read()
    return first_file_content


def second_file() -> str:
    with open(FILE_2, "rb") as second:
        second_file_content = second.read()
    return second_file_content


# first = first_file
# second = second_file


def change_content(first_file, second_file):
    with open(FILE_1, "wb") as file_1:
        file_1.write(second_file)
    with open(FILE_2, "wb") as file_2:
        file_2.write(first_file)
    return first_file, second_file


# change_content(first_file(), second_file())
