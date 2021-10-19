#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Самостоятельно проработайте пример с оптимизацией хвостовых вызовов в Python.
С помощью пакета  timeit  оцените скорость работы функций  factorial  и  fib
с использованием интроспекции стека и без использования интроспекции стека.
"""

from timeit import timeit


# Рекурсивное нахождение факториала
test_fac = """
def fac_recursion(n):

    if n == 0:
        return 1

    return fac_recursion(n - 1) * n
"""


# Рекурсивное нахождение числа Фибоначи
test_fib = """
def fib_recursion(n):

    if n in (1, 2):
        return 1

    return fib_recursion(n - 1) + fib_recursion(n - 2)
"""


test_fac_optimized = """
class TailRecurseException:
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


def tail_call_optimized(g):

    def func(*args, **kwargs):

        f = sys._getframe()

        while f and f.f_code.co_filename == f: #############
            raise TailRecurseException(args, kwargs)
        else:
            while True:
                try:
                    return g(*args, **kwargs)
                except TailRecurseException as e:
                    args = e.args
                    kwargs = e.kwargs

    func.__doc__ = g.__doc__
    return func


@tail_call_optimized
def fac_recursion(n):

    if n == 0:
        return 1

    return fac_recursion(n - 1) * n
"""


test_fib_optimized = """
class TailRecurseException:

    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


def tail_call_optimized(g):

    def func(*args, **kwargs):
        f = sys._getframe()
        while f and f.f_code.co_filename == f: ###########
            raise TailRecurseException(args, kwargs)
        else:
            while True:
                try:
                    return g(*args, **kwargs)
                except TailRecurseException as e:
                    args = e.args
                    kwargs = e.kwargs

    func.__doc__ = g.__doc__
    return func


@tail_call_optimized
def fib_recursion(n):

    if n in (1, 2):
        return 1

    return fib_recursion(n - 1) + fib_recursion(n - 2)
"""


if __name__ == '__main__':

    print("Время выполнения функции factorial: ",
          timeit(test_fac, number=1000))
    print("Время выполнения функции factorial c"
          " оптимизацией хвостовой рекурсии: ",
          timeit(test_fac_optimized, number=1000))
    print("Время выполнения функции fib: ",
          timeit(test_fib, number=1000))
    print("Время выполнения функции fib c"
          " оптимизацией хвостовой рекурсии: ",
          timeit(test_fib_optimized, number=1000))
