from unicodedata import decimal
import numpy as np
import math
B = [[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, -1, -1, -1, -1], [1, 1, -1, -1, 0, 0, 0,  0], [0, 0, 0, 0, 1,  1, -1, -1],
     [1, -1, 0, 0, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0, 0,  0], [0, 0, 0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 0, 0, 1, -1]]
B = np.array(B)
B = B.T
eo = np.dot(B.T, B)


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


def normalizajcaWektora(vector):
    # print(vector)
    # print(dlugosc(vector))
    # print(vector/dlugosc(vector))
    return vector/dlugosc(vector)


def normalizacjaWMacierzy(B):
    X = []
    B = B.T
    for i in range(len(B)):
        X.append(normalizajcaWektora(B[i]))
    return np.array(X)


print(B)
print(eo)
print(czyOrtogonalna(eo))

C = normalizacjaWMacierzy(B)
xd = np.round(np.dot(C.T, C), decimals=5)
print(C)
print(xd)
