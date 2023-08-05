"""
Написать обычную функцию для факториала, генератор и
рекурсию. Сравнить их время работы
"""

import functools
import time


def timer(func):
    """
    Simple timer
    """
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        runtime = time.perf_counter() - start
        print(f"{func.__name__} took {runtime:.7f} secs")
        return result

    return _wrapper


@timer
def rec_factorial(digit):
    """
    Find factorial via recursion
    """
    if digit == 1:
        return 1
    return rec_factorial(digit - 1) * digit


@timer
def gen_factorial(num):
    """
    Find factorial via generator
    """
    # start_gen = time.perf_counter()
    factorial = 1
    for fac in range(1, num + 1):
        factorial *= fac
    # end_gen = time.perf_counter() - start_gen
    yield factorial


@timer
def simple_factorial(a):
    """
    Find factorial via simple func
     """
    b = 1
    if a == 1:
        return 1
    if a > 1:
        for i in range(1, a + 1):
            b *= i
    return b


print(rec_factorial(5))
for i in gen_factorial(5):
    print(i)
print(simple_factorial(5))
