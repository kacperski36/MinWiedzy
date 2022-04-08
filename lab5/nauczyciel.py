import math as m
import numpy as np
import random

lista = []
with open("lab3\\australian.dat", "r") as file:
    for line in file:
        tmp = line.split()
        wynik = list(map(lambda a: float(a), tmp))
        lista.append(wynik)


def metrykaEuklidesowa(p1, p2):
    vector1 = np.array(p1[:-1])
    vector2 = np.array(p2[:-1])
    wynik = vector1 - vector2
    return m.sqrt(np.dot(wynik, wynik))


def wagaKropki(element):
    return element[len(element)-1]


def najmniejsza(lista):
    n = lista[0]
    id = 0
    for i in range(1, len(lista)):
        if lista[i] < n:
            n = lista[i]
            id = i
    return [n, id]


def srodek(lista):
    for i in range(len(lista)):
        lista[i][len(lista[i])-1] = float(random.randint(0, 1))
    suma0 = 0
    suma1 = 0
    wynik0 = []
    wynik1 = []
    for i in range(len(lista)):
        for j in range(len(lista)):
            if wagaKropki(lista[i]) == wagaKropki(lista[j]) and wagaKropki(lista[j]) == 1:
                suma1 += metrykaEuklidesowa(lista[i], lista[j])
            elif wagaKropki(lista[i]) == wagaKropki(lista[j]) and wagaKropki(lista[j]) == 0:
                suma0 += metrykaEuklidesowa(lista[i], lista[j])
        if suma0 != 0:
            wynik0.append(suma0)
            suma0 = 0
        elif suma1 != 0:
            wynik1.append(suma1)
            suma1 = 0
    id0 = najmniejsza(wynik0)[1]
    id1 = najmniejsza(wynik1)[1]
    for i in range(10):
        for j in range(len(lista)):
            if metrykaEuklidesowa(lista[id0], lista[j]) < metrykaEuklidesowa(lista[id1], lista[j]):
                lista[j][len(lista[i])-1] = 0.0
            elif metrykaEuklidesowa(lista[id0], lista[j]) > metrykaEuklidesowa(lista[id1], lista[j]):
                lista[j][len(lista[i])-1] = 1.0
    return lista


def zeroJeden(lista):
    zero = 0
    jeden = 1
    for i in range(len(lista)):
        if wagaKropki(lista[i]) == 0:
            zero += 1
        elif wagaKropki(lista[i]) == 1:
            jeden += 1
    print(zero)
    print(jeden)


# srodek(lista)
zeroJeden(srodek(lista))
