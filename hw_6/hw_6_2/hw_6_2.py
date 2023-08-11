"""Дан файл целых чисел. Создать два новых файла, первый из которых
содержит четные числа из исходного файла, а второй — нечетные (в том
же порядке). Если четные или нечетные числа в исходном файле
отсутствуют, то соответствующий результирующий файл оставить
пустым."""
with open("hw_6_2.txt") as f:
    digit_list = list(map(int, f.readline().split()))


def odd_and_even():
    """
    Checks digits from a list and sorts them by evenness and oddness
    """
    even_digits = []
    odd_digits = []
    for i in digit_list:
        if i % 2 == 0:
            even_digits.append(i)
            with open("even.txt", "w") as even:
                even.writelines(str(even_digits))
        elif i % 2 != 0:

            odd_digits.append(i)
            with open("odd.txt", "w") as odd:
                odd.writelines(str(odd_digits))
        else:
            pass


odd_and_even()
