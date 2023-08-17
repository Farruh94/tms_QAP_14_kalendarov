
# 1 Создать lambda функцию, которая принимает на вход
# имя и выводит его в формате “Hello, {name}”

user_name = lambda name: f"Hello, {name}"

print(user_name("John Wick"))

# Создать lambda функцию, которая принимает на вход
# список имен и выводит их в формате “Hello, {name}” в
# другой список
user_list = ["Luck", "Farruh"]
new_list = list(map(lambda x: f"Hello, {x}", user_list))

print(new_list)
