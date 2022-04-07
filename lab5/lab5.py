import math as m
import numpy as np

lista = []
with open("lab3\\australian.dat", "r") as file:
    for line in file:
        tmp = line.split()
        wynik = list(map(lambda a: float(a), tmp))
        lista.append(wynik)
# print(lista)


def metrykaEuklidesowa(p1, p2):
    vector1 = np.array(p1)
    vector2 = np.array(p2)
    wynik = vector1 - vector2
    return m.sqrt(np.dot(wynik, wynik))


xd = [3, 3, 4, 2]


def srednia(lista):
    v1 = np.array(lista)
    suma = sum(v1)
    return suma/len(v1)


def wariancja(lista):
    v = np.array(lista)
    v = v - srednia(lista)
    return np.dot(v, v)/len(v)


def odchylenie(lista):
    return m.sqrt(wariancja(lista))


print(srednia(xd))
print(odchylenie(xd))
print(wariancja(xd))
nowy = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
