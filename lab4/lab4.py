import math as m
import numpy as np
import random

lista = []
with open("lab3\\australian.dat", "r") as file:
    for line in file:
        tmp = line.split()
        wynik = list(map(lambda a: float(a), tmp))
        lista.append(wynik)
# print(lista)


# def metryka(a, b):
#     wynik = 0
#     for i in range(len(a)-1):
#         wynik += (a[i] - b[i])**2
#     return m.sqrt(wynik)


def metrykaEuklidesowa(p1, p2):
    vector1 = np.array(p1[:-1])
    vector2 = np.array(p2[:-1])
    wynik = vector1 - vector2
    return m.sqrt(np.dot(wynik, wynik))

# print(metryka(lista[0], lista[1]))
# print(metryka(lista[0], lista[2]))
# print(metryka(lista[0], lista[3]))


def grupowanie(lista, who, index):
    wynik = dict()
    y = lista[who]
    for i in range(1, len(lista)):
        decyzja = lista[i][index]
        if decyzja in wynik.keys():
            wynik[decyzja].append(metrykaEuklidesowa(y, lista[i]))
        else:
            wynik[decyzja] = [metrykaEuklidesowa(y, lista[i])]
    return wynik

# print(grupowanie(lista, 0, 3))


def grupowanieDoTupla(x, lista):
    wynik = []
    for i in range(0, len(lista)):
        odleglosc = metrykaEuklidesowa(lista[i], x)
        wynik.append((lista[i][len(lista[i])-1], odleglosc))
    return wynik


nowy = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
grupowanieDoTuplaWynik = grupowanieDoTupla(nowy, lista)

# print(grupowanieDoTuplaWynik)


def ListaToSlownik(lista):
    wynik = dict()
    for item in lista:
        decyzja = item[0]
        if decyzja not in wynik.keys():
            wynik[decyzja] = []
        wynik[decyzja].append(item[1])
    return wynik


slownik = ListaToSlownik(grupowanieDoTuplaWynik)
# print(slownik)


def kNajmniejszych(k, slownik):
    wynik = dict()
    for key in slownik:
        sortedDict = sorted(slownik[key])
        sortedDict = sortedDict[:k]
        wynikSum = sum(sortedDict)
        wynik[key] = wynikSum
    return wynik


# print(kNajmniejszych(5, slownik))

# Praca domowa


def decyzja(who, lista, k):
    pogrupowane = grupowanieDoTupla(who, lista)
    slownikGrupa = ListaToSlownik(pogrupowane)
    najmniejsze = kNajmniejszych(k, slownikGrupa)

    klucze = list(najmniejsze.keys())
    klasaDecyzyjnaWynik = klucze[0]
    ilosc = 1
    for i in range(1, len(klucze)):
        if najmniejsze[klucze[i]] == najmniejsze[klasaDecyzyjnaWynik]:
            ilosc += 1
        elif najmniejsze[klucze[i]] < najmniejsze[klasaDecyzyjnaWynik]:
            klasaDecyzyjnaWynik = klucze[i]
            ilosc == 1
    if ilosc > 1:
        return
    else:
        return klasaDecyzyjnaWynik


# print(decyzja(nowy, lista, 5))

# def srodekMasy(lista):
#     for i in range(len(lista)):
#         for j in range(len(lista)):
#             if lista[i][len(lista[i])-1] == 1 and lista[j][len(lista[j])-1] == 1:

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
            if wagaKropki(lista[i]) == wagaKropki(lista[j]) and wagaKropki(lista[i]) == 1:
                suma1 += metrykaEuklidesowa(lista[i], lista[j])
            elif wagaKropki(lista[i]) == wagaKropki(lista[j]) and wagaKropki(lista[i]) == 0:
                suma0 += metrykaEuklidesowa(lista[i], lista[j])
        if suma0 != 0:
            wynik0.append(suma0)
        elif suma1 != 0:
            wynik1.append(suma1)
# tu zrobić for na 10 iteracji ze sprawdzaniem odległości od kroperk i przypisać wartości

    print(najmniejsza(wynik0))
    print(najmniejsza(wynik1))


srodek(lista)

#odegłość  - metryka
# 28.02 nagranie 1h 10 min nagranie


# napisz funkcje kótra całkuje metodą monte carlo

# Do domu:
# Całkowanie numeryczne
# Pole pod krzywą całkę oznaczoną
# Wyznaczyć ograniczenie górne f(x) = y1
# maximum razy dwa
# (b-a)*y pole prostokąta
# całkowanie metoda monte carlo
#

# dziele na dwie części
# metoda prostokątów
# metoda trapezów
