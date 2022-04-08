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
        if(ry <= func(rx)):
            wynik += 1
    return (x2-x1)*(max-min)*(wynik/points)


def prostokat(fun, x1, x2, num=10):
    wynik = 0
    react = 2 ** num
    width = ((x2 - x1) / react)
    for i in range(react):
        xd = x1 + (width * i) + width / 2
        wynik += fun(xd) * width
    return wynik


def funkcja(x):
    return x


print(monteCarlo(funkcja, 0, 1))
print(prostokat(funkcja, 0, 1))
