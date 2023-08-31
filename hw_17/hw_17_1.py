# Дан файл вещественных чисел. Заменить в нем все элементы на их
# квадраты.
FILE = "./hw_17/files_1/digits.txt"

with open(FILE, "r") as f:
    list_of_digits = list(map(float, f.readline().split()))


def squaring():
    final_result = []
    for i in list_of_digits:
        i = round(i ** 2, 2)
        final_result.append(i)
    return final_result


# squared_digits = squaring


def writing_to_file(squaring):
    file_content = ""
    for i in squaring:
        i = round(i, 2)
        file_content = str(file_content) + " " + str(i)
        file_content.lstrip()
    with open(FILE, "w") as file:
       file.write(str(file_content))
    with open(FILE, "r") as f:
        content_1 = f.readline()
    return content_1


print(writing_to_file(squaring()))

# writing_to_file(squaring())
digits = "10.3 11.2 25.6 30.5"


def rewrite_to_file():
    with open(FILE, "w") as file_1:
        file_1.write(digits)
    with open(FILE, "r") as oc:
        old_content = oc.readline()
    return old_content

old = rewrite_to_file()
