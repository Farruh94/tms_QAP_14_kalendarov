# 4 Даны два файла произвольного типа. Поменять местами их
# содержимое. Файлы должны быть бинарного типа
FILENAME_1 = "first.bin"
FILENAME_2 = "second.bin"

def write_to_first_file():
    first_data = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et " \
                 "dolore magna aliqua."
    en = first_data.encode()
    with open(FILENAME_1, "wb") as file:
       file.write(en)

write_to_first_file()


with open(FILENAME_1, "rb") as file:
    r = file.read()
    print(r)

def write_to_second_file():
    second_data = 48598457405042504567
    enc = str(second_data).encode()
    with open(FILENAME_2, "wb") as f:
        f.write(enc)

write_to_second_file()

with open(FILENAME_2, "rb") as f:
    rd = f.read()
    print(rd)

def change_content():
    with open(FILENAME_1, "wb") as file_1:
        file_1.write(rd)
    with open(FILENAME_2, "wb") as file_2:
        file_2.write(r)

change_content()

with open(FILENAME_1, "rb") as fb:
    c = fb.read()
    print(c)

with open(FILENAME_2, "rb") as fc:
    d = fc.read()
    print(d)