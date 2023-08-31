import os

FILE_1 = "./hw_17/files_1/digits.txt"


def check_file():
    if os.path.exists("./files_1/text.txt"):
        txt_file = True
    else:
        txt_file = False
    return txt_file

def read_from_file():
    with open(FILE_1, "r") as file_1:
        digit_list = file_1.read()
    return digit_list
