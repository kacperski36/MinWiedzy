import random
import math


def monteCarlo(func, x1, x2, points=500):
    max = func(x2)
    min = 0
    if func(x1) < 0:
        min = func(x1)
    wynik = 0
    for i in range(points):
        rx = random.uniform(x1, x2)
        ry = random.uniform(min, max)
        result = func(rx)
        if(ry <= result):
            wynik += 1
    return (x2-x1)*(max-min)*(wynik/points)


def probkowanie(fun, x1, x2, react=10):
    wynik = 0
    num = 2 ** react
    width = ((x2 - x1) / num)
    for i in range(num):
        xd = x1 + (width * i) + width / 2
        wynik += fun(xd) * width
    return wynik


def f(x):
    return x**2


print(probkowanie(f, 6, 13, 15))


def funkcja(x):
    return x**2


print(monteCarlo(funkcja, 5, 10))
