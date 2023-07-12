# 1 Напишите генератор который принимает список
# numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7] и
# возвращает новый список только с положительными
# числами



def pos_number():
    numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
    for i in numbers:
        if i > 0:
            yield i

positive_list = []
for i in pos_number():
    positive_list.append(i)

print(positive_list)



# 2 Необходимо составить список чисел которые
# указывают на длину слов в строке: sentence = " thequick
# brown fox jumps over the lazy dog", но только если слово
# не "the" с обработкой исключений

class MyError(Exception):
    def __init__(self, text):
        self.txt = text



def findLen():
    str = "thequick brown fox jumps over the lazy dog"
    some_lst = iter(str.split(" "))
    random_str = 'the'
    word_len = 0
    for i in some_lst:
        try:
            if random_str in i:
                raise MyError(f"В слове, {i} содержится '{random_str}'")
            else:
                word_len = len(i)
                yield word_len, i

        except MyError as my_error:
            print(my_error)


for j in findLen():
    print(j, end="\n")
