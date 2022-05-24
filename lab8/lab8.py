from unicodedata import decimal
import numpy as np
import math
B = [[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, -1, -1, -1, -1], [1, 1, -1, -1, 0, 0, 0,  0], [0, 0, 0, 0, 1,  1, -1, -1],
     [1, -1, 0, 0, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0, 0,  0], [0, 0, 0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 0, 0, 1, -1]]

wektor = [8, 6, 2, 3, 4, 6, 6, 5]
B = np.array(B)
B = B.T
B2 = np.dot(B.T, B)


def dlugosc(vector):
    result = 0
    for i in range(len(vector)):
        result += vector[i]**2
    return math.sqrt(result)


def czyOrtogonalna(B):
    A = np.dot(B.T, B)
    for i in range(len(A)):
        for j in range(len(A[0])):
            if i != j and A[i][j] != 0:
                return False
    return True


def czyOrtonormalna(B):
    C = np.round(np.dot(B.T, B), decimals=5)
    return czyJednostkowa(C)


def czyJednostkowa(B):
    for i in range(len(B)):
        for j in range(len(B[0])):
            if i == j and B[i][j] != 1:
                return False
    return True


def normalizajcaWektora(vector):
    return vector/dlugosc(vector)


def normalizacjaWMacierzy(B):
    X = []
    B = B.T
    for i in range(len(B)):
        X.append(normalizajcaWektora(B[i]))
    return np.array(X)


def wektorPrzezMacierz(wektor, bazaP, bazaN):
    if czyOrtonormalna(bazaN):
        if czyJednostkowa(bazaP):
            return np.dot(bazaN.T, wektor)
        return np.dot(np.dot(bazaN.T, bazaP), wektor)
    return np.dot(np.dot(np.linalg.inv(bazaN), bazaP), wektor)


print(B)

print(czyOrtogonalna(B2))

C = normalizacjaWMacierzy(B)

print(czyJednostkowa(C))
