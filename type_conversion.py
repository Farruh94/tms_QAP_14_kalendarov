# Преобразование типов
# 1
# Перевести строку в массив
# "Robin Singh" => ["Robin”, “Singh"]
str1 = "Robin Singh"
print(str1.split())
# "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]
my_str = "I love arrays they are my favorite"
str_to_array = my_str.split()
print(str_to_array)
# 2
# Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
my_array = ["Ivan", "Ivanov"]
city = "Minsk"
country = "Belarus"
print(f"Привет," + " " + ' '.join(my_array) + "!" + " " + "Добро пожаловать в " + city + " " + country)

# 3
# Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] сделайте из него
# строку => "I love arrays they are my favorite"
print(' '.join(str_to_array))
# 4
# Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6
my_dict = {"a": 1, "b": 2, "c": 11, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10}
my_dict.pop("f")
print(my_dict)
# 5
# Есть 2 словаря

# Необходимо их объединить по ключам, а значения ключей поместить в список, если у
# одного словаря есть ключ "а", а у другого нет, то поставить значение None на
# соответствующую позицию(1-я позиция для 1-ого словаря, вторая для 2-ого)
# ab = {'a': [1, None], 'b': [2, None], 'c': [3, 3], 'd': [None, 4], 'e': [None, 5]}
a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}
ab = {}

def join_dicts():
    for key in set(list(a.keys()) + list(b.keys())):
        ab[key] = [a.get(key), b.get(key)]
    return ab

print(join_dicts())

# *1) Вам передан массив чисел. Известно, что каждое число в этом массиве имеет пару,
# кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
# Напишите программу, которая будет выводить уникальное число
in_list = [1, 5, 2, 9, 2, 9, 1]

for e in in_list:
    if in_list.count(e) < 2:
        print(e)

# *2) Дан текст, который содержит различные английские буквы и знаки препинания. Вам
# необходимо найти самую частую букву в тексте. Результатом должна быть буква в
# нижнем регистре.
# При поиске самой частой буквы, регистр не имеет значения, так что при подсчете
# считайте, что "A" == "a". Убедитесь, что вы не считайте знаки препинания, цифры и
# пробелы, а только буквы.
# Если в тексте две и больше буквы с одинаковой частотой, тогда результатом будет
# буква, которая идет первой в алфавите. Для примера, "one" содержит "o", "n", "e" по
# одному разу, так что мы выбираем "e".
# "a-z" == "a"
# "Hello World!" == "l"
# "How do you do?" == "o"
# "One" == "e"
# "Oops!" == "o"
# "AAaooo!!!!" == "a"
# "a" * 9000 + "b" * 1000 == "a"

dict_1 = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0,
          "o": 0, "p": 0,
          "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
text_1 = "How do you do?"
text_1 = text_1.lower()
d = 0
keys = dict_1.keys()
for i in text_1:
    if text_1.count(i) >= 1:
        if i in keys:
            d = dict_1.get(i, 0)
            dict_1[i] = d + 1
print(max(dict_1, key=dict_1.get))
