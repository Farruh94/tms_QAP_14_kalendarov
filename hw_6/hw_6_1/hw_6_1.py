# Дан файл целых чисел, содержащий не менее четырех элементов.
# Вывести первый, второй, предпоследний и последний элементы данного
# файла. Если чисел меньше 3 выводить ошибку
nums = 11, 23, 33, 45
with open("hw_6_1.txt", "w") as f:
    f.write(str(nums))

with open("hw_6_1.txt", "r") as f:
    a = f.read()
    print(a.count(','))

def numbers():
    if a.count(",") >= 2:
        return a
    else:
        return "В файле меньше 3 чисел"

print(numbers())