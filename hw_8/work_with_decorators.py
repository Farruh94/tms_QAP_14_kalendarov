"""
Напишите декоратор, который проверял бы тип параметров
функции, конвертировал их если надо и складывал:
"""
def types(type):
    def decorator(func):
        def inner(*args):
            return func(*(map(eval(type), args)))
        return inner
    return decorator

@types(type='int')
def add_two_symbols(a, b, c):
    return a + b + c

print(add_two_symbols(0.1, 0.2, 0.3))

@types(type="str")
def add_two_symbols(a, b, c):
    return a + b + c

print(add_two_symbols(0.1, 0.2, 0.3))
