import os

FILENAME_1 = "./hw_17/files_1/first.bin"
FILENAME_2 = "./hw_17/files_1/second.bin"
PATH = "./hw_17/files_1"


def first_changed():
    with open(FILENAME_1, 'rb') as f1:
        f1_text = f1.read()
    return f1_text


def second_changed():
    with open(FILENAME_2, 'rb') as f2:
        f2_text = f2.read()
    return f2_text


changed_1 = first_changed
changed_2 = second_changed


def check_if_first_file_exist():
    if os.path.exists("bin_file.bin"):
        file_1 = True
    else:
        file_1 = False
    return file_1


def check_if_second_file_exist():
    if os.path.exists("second_bin.bin"):
        file_2 = True
    else:
        file_2 = False
    return file_2


first_exist = check_if_first_file_exist
second_exist = check_if_second_file_exist


def not_exist_1():
    with open("bin_file.bin", 'rb') as not_exist_file_1:
        str_1 = not_exist_file_1.read()
    return str_1


def not_exist_2():
    with open("../hw_6/hw_6_4/files/second.bin", "rb") as not_exist_file_2:
        str_2 = not_exist_file_2.read()
    return str_2


not_exist_file_1 = not_exist_1
not_exist_file_2 = not_exist_2


def incorrect_format():
    txt_list = []
    for address, dirs, files in os.walk(PATH):
        for name in files:
            if name.endswith(".txt"):
                txt_list.append(os.path.join(address, name))
    return txt_list


def incorrect_files(incorrect_format):
    files = ""
    for i in incorrect_format:
        if i in incorrect_format:
            files = False
    return files


print(incorrect_files(incorrect_format()))
# not_valid_files = incorrect_files(incorrect_format)
