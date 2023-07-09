# Дан файл вещественных чисел. Заменить в нем все элементы на их
# квадраты.

with open("hw_6_3.txt", "r") as f:
    b = list(map(float, f.readline().split()))



def  float_to_int():
    c = []
    d = 0
    for i in b:
        d = i ** 2
        c.append(int(d))
        with open("hw_6_3.txt", "w") as file:
            file.write(str(c))

float_to_int()