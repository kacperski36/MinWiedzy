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
    v2 = np.ones(len(v1))
    suma = np.dot(v2, v1)
    return suma/len(v1)


def wariancja(lista):
    v1 = np.array(lista)
    v2 = np.ones(len(v1)) * srednia(lista)
    roznica = v1-v2
    return np.dot(roznica, roznica)/len(v1)


def odchylenie(lista):
    return m.sqrt(wariancja(lista))


print(srednia(xd))
print(wariancja(xd))
print(odchylenie(xd))
