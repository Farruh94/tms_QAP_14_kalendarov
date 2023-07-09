# Дан файл целых чисел. Создать два новых файла, первый из которых
# содержит четные числа из исходного файла, а второй — нечетные (в том
# же порядке). Если четные или нечетные числа в исходном файле
# отсутствуют, то соответствующий результирующий файл оставить
# пустым.
with open("hw_6_2.txt") as f:

     b = list(map(int, f.readline().split()))


def odd_and_even():
    a = []
    c = []
    for i in b:
        if i % 2 == 0:
            a.append(i)
            with open("even.txt", "w") as e:
                e.writelines(str(a))
        elif i % 2 != 0:

            c.append(i)
            with open("odd.txt", "w") as o:
                o.writelines(str(c))
        else:
            pass


odd_and_even()