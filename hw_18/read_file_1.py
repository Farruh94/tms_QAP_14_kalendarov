import os

BASE_DIR = os.path.abspath(os.getcwd())
FILE = os.path.abspath(os.path.join(BASE_DIR, './hw_18/files_2/digits.txt'))


def check_file():
    if os.path.exists(FILE):
        txt_file = True
    else:
        txt_file = False
    return txt_file

def read_from_file():
    with open(FILE, "r") as file_1:
        digit_list = file_1.read()
    return digit_list
print(read_from_file())
