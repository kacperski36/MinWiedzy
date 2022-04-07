import math as m
lista = []
with open("lab3\\australian.dat", "r") as file:
    for line in file:
        tmp = line.split()
        wynik = list(map(lambda a: float(a), tmp))
        lista.append(wynik)
print(lista)


def metryka(a, b):
    wynik = 0
    for i in range(len(a)-1):
        wynik += (a[i] - b[i])**2
    return m.sqrt(wynik)


print(metryka(lista[0], lista[1]))
print(metryka(lista[0], lista[2]))
print(metryka(lista[0], lista[3]))


def grupowanie(lista, who, index):
    wynik = dict()
    y = lista[who]
    for i in range(1, len(lista)):
        decyzja = lista[i][index]
        if decyzja in wynik.keys():
            wynik[decyzja].append(metryka(y, lista[i]))
        else:
            wynik[decyzja] = [metryka(y, lista[i])]
    return wynik


print("===== PD ======")
print(grupowanie(lista, 0, 3))
# Zadanie domowe:
#y= lista[0]
#d(y,x) - odległość
# x nalezy do listy bez 0 indexu
# słownik - klucz: klasa decyzyjna, wartość: lista z odległościami
# klasa decyzyjna - ostatni element listy


# obliczanie wyznacznika z dowolnej macierzy kwadratowe
