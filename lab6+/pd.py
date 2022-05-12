import numpy as np
import math

# A = np.array([[1, 0], [1, 1], [0, 1]])
# A = np.array([[1, 0], [1, 1], [1, 1]])
A = np.array([[0, 1], [2, 3], [4, 5]])
# A = np.array([[3, 2], [1, 5], [1, 0]])
# A = np.array([[3, 2], [1, 5]])


def dlugosc(vector):
    result = 0
    for i in range(len(vector)):
        result += vector[i]**2
    return math.sqrt(result)


def projekcja(u, v):
    l = np.dot(v.T, u)
    m = np.dot(u.T, u)
    return (l/m)*u


def dekompozycja(A):
    Q = []
    v1 = []
    v2 = []
    for i in range(len(A)):
        v1.append(A[i][0])
        v2.append(A[i][1])
    u1 = np.array(v1)
    v2 = np.array(v2)
    e1 = u1/dlugosc(u1)
    Q.append(e1)
    u2 = v2 - projekcja(u1, v2)
    e2 = u2/dlugosc(u2)
    Q.append(e2)
    Q = np.array(Q)
    return np.array(Q.T)


Q = dekompozycja(A)
R = np.round(np.dot(Q.T, A), decimals=5)
wynik = np.round(np.dot(Q, R), decimals=5)


def a_plus_k(A, k):
    Q = dekompozycja(A)
    if len(A) == len(A[0]):
        for i in range(k):
            Q = dekompozycja(A)
            R = np.round(np.dot(Q.T, A), decimals=5)
            A = np.round(np.dot(R, Q), decimals=5)
    return A


def wartosci_wlasne(A):
    new_A = A
    while (np.diag(new_A) - np.dot(new_A, np.ones((len(new_A), 1))).T).all() > 0.001:
        new_A = a_plus_k(new_A, 1)
    return np.diag(new_A)


# ak = a_plus_k(A, 10)
print(A)
print(Q)
# print(R)
# print(wynik)
# print(ak)
# wynik = wartosci_wlasne(A)
# print(wynik)
