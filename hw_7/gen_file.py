"""
1 Напишите генератор, который принимает список
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7] и
возвращает новый список только с положительными
числами
"""



def pos_number():
    """
    Generator that return only positive numbers
    """
    numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
    for number in numbers:
        if number > 0:
            yield number


positive_list = []
for i in pos_number():
    positive_list.append(i)

print(positive_list)


# 2 Необходимо составить список чисел которые
# указывают на длину слов в строке: sentence = " thequick
# brown fox jumps over the lazy dog", но только если слово
# не "the" с обработкой исключений

class MyError(Exception):
    """
    My own exception
    """
    def __init__(self, text):
        self.txt = text


def find_len():
    """
    Measure len of words on sentence
    """
    sentence = "thequick brown fox jumps over the lazy dog"
    some_lst = iter(sentence.split(" "))
    exception_str = 'the'
    for word in some_lst:
        try:
            if exception_str in word:
                raise MyError(f"В слове, {word} содержится '{exception_str}'")
            else:
                word_len = len(word)
                yield word_len, word

        except MyError as my_error:
            print(my_error)


for j in find_len():
    print(j, end="\n")
