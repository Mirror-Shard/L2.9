#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Самостоятельно изучите работу со стандартным пакетом Python  timeit.
Оцените с помощью этого модуля скорость работы итеративной и рекурсивной
версий функций factorial  и  fib
"""

from timeit import timeit


# Итеративное нахождение числа Фибоначи
test_fib_iteration = """
def fib_iteration(x):

    fib1 = fib2 = 1
    n = x - 2

    while n > 0:
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1

    return fib2
"""


# Рекурсивное нахождение числа Фибоначи
test_fib_recursion = """
def fib_recursion(n):

    if n in (1, 2):
        return 1

    return fib_recursion(n - 1) + fib_recursion(n - 2)
"""


# Нахождение числа Фибоначи с декоратором
test_fib_decorator = """
from functools import lru_cache
@lru_cache

def fib_decorator(n):
    if n in (1, 2):
        return 1

    return fib_decorator(n - 1) + fib_recursion(n - 2)
"""

# Итеративное нахождение факториала
test_fac_iteration = """
def fac_iteration(n):

    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1

    return factorial
"""


# Рекурсивное нахождение факториала
test_fac_recursion = """
from functools import lru_cache
@lru_cache

def fac_recursion(n):

    if n == 0:
        return 1

    return fac_recursion(n - 1) * n
"""


# Нахождение факториала с декоратором
test_fac_decorator = """
def fac_decorator(n):

    if n == 0:
        return 1

    return fac_decorator(n - 1) * n
"""


if __name__ == '__main__':

    # Выводит время выполнения чисел Фибоначи
    print("Время выполнения итеративной функции числа Фибоначи: ",
          timeit(test_fib_iteration, number=100)/100)
    print("Время выполнения рекурсивной функции числа Фибоначи: ",
          timeit(test_fib_recursion, number=100)/100)
    print("Время выполнения декоративной функции числа Фибоначи: ",
          timeit(test_fib_decorator, number=100) / 100)

    # Выводит время выполнения факториалов
    print("Время выполнения итеративной функции факториала: ",
          timeit(test_fac_iteration, number=100)/100)
    print("Время выполнения рекурсивной функции факториала: ",
          timeit(test_fac_recursion, number=100)/100)
    print("Время выполнения декоративной функции факториала: ",
          timeit(test_fac_decorator, number=100) / 100)
