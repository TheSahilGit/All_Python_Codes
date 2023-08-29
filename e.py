import matplotlib.pyplot as plt
import numpy as np
import math
import random


def pi():
    step = 100000
    p = 0
    for n in range(step):
        p = p + 4 * (-1) ** n / (2 * n + 1)
    return p


def factorial(n):
    fact = 1
    if n == 0:
        return fact
    else:
        for i in range(1, n + 1):
            fact = fact * i
        return fact


def exponential(x):
    e = 0
    step = 1000
    for n in range(step):
        e = e + x ** n / factorial(n)
    return e


def sin(x):
    s = 0
    step = 10
    x_rad = x * pi() / 180.0
    for n in range(step):
        s = s + ((-1) ** n) * (x_rad ** (2 * n + 1)) / factorial(2 * n + 1)
    return s


def cos(x):
    c = 0
    step = 10
    x_rad = x * pi() / 180.
    for n in range(step):
        c = c + ((-1) ** n) * (x_rad ** (2 * n)) / factorial(2 * n)
    return c


def tan(x):
    t = float(sin(x) / cos(x))
    return t


def cot(x):
    c = float(1 / tan(x))
    return c


def sec(x):
    s = float(1 / cos(x))
    return s


def cosec(x):
    c = float(1 / sin(x))
    return c


## This needs modificaion ##
def quadratic_nsolve(a, b, c):
    def f(x):
        return a * x ** 2 + b * x + c

    def solve_loop(x0, x1):

        if b ** 2 - 4 * a * c < 0:
            print("No real root.")
        if b ** 2 - 4 * a * c == 0:
            print(-b / 2.0)

        else:
            step = 1000
            for i in range(step):
                x2 = float((x1 + x0) / 2.0)

                if f(x2) * f(x0) < 0:
                    x1 = x2
                else:
                    x0 = x2

            if abs(f(x2)) < 0.0001:
                print(x2)

    solve_loop(-20, 10000)
    solve_loop(-10000, 0)
quadratic_nsolve(1,10,5)

