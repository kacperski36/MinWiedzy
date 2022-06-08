import numpy as np
import math

# A = np.array([[1, 0], [1, 1], [0, 1]])
# A = np.array([[1, 0], [1, 1], [1, 1]])
# A = np.array([[0, 1], [2, 3], [4, 5]])
# A = np.array([[3, 2, 1], [1, 5, 0], [1, 0, 4]])
A = np.array([[1, 2, 2], [2, 8, 0], [2, 0, 4]])
B = np.array([[1, 1], [0, 1], [-1, 1]])
D = np.array([[1, -2, 0], [0, -2, 1]])


def dlugosc(vector):
    result = 0
    for i in range(len(vector)):
        result += vector[i]**2
    return math.sqrt(result)


def projekcja(u, v):
    l = np.dot(v.T, u)
    m = np.dot(u.T, u)
    return (l/m)*u


def macierzQR(A):
    proj = 0
    all_v = []
    all_u = []
    Q = []
    for i in range(len(A[0])):
        v = []
        for j in range(len(A)):
            v.append(A[j][i])
        all_v.append(v)
    for vi in all_v:
        v = np.array(vi)
        if len(all_u) == 0:
            all_u.append(v)
            u = np.array(all_u[0])
            e = u/dlugosc(u)
            Q.append(e)
        else:
            u = np.array(all_u[-1])
            proj += projekcja(u, v)
            u = v-proj
            all_u.append(u)
            e = u/dlugosc(u)
            Q.append(e)
    Q = np.array(Q)
    Q = Q.T
    R = np.round(np.dot(Q.T, A), decimals=5)
    return Q.T, R


def a_plus_k(A, k):
    if len(A) == len(A[0]):
        for i in range(k):
            Q, R = macierzQR(A)
            A = np.round(np.dot(R, Q), decimals=5)
    return A


def wartosci_wlasne(A):
    A2 = A
    while (np.diag(A2) - np.dot(A2, np.ones((len(A2), 1))).T).all() > 0.001:
        A2 = a_plus_k(A2, 1)
    return np.round(np.diag(A2), decimals=0)


print(D)
C = np.dot(D.T, D)
print(C)
print(wartosci_wlasne(C))
print(np.dot(C, np.ones((len(C), 1))).T)
