import numpy as np
import math

# A = np.array([[1, 0], [1, 1], [0, 1]])
# A = np.array([[1, 0], [1, 1], [1, 1]])
# A = np.array([[0, 1], [2, 3], [4, 5]])
A = np.array([[3, 2, 1], [1, 5, 0], [1, 0, 4]])


def dlugosc(vector):
    result = 0
    for i in range(len(vector)):
        result += vector[i]**2
    return math.sqrt(result)


def projekcja(u, v):
    l = np.dot(v.T, u)
    m = np.dot(u.T, u)
    return (l/m)*u


def macierzQ(A):
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
    return Q.T


def a_plus_k(A, k):
    Q = macierzQ(A)
    if len(A) == len(A[0]):
        for i in range(k):
            Q = macierzQ(A)
            R = np.round(np.dot(Q.T, A), decimals=5)
            A = np.round(np.dot(R, Q), decimals=5)
    return A


def wartosci_wlasne(A):
    new_A = A
    while (np.diag(new_A) - np.dot(new_A, np.ones((len(new_A), 1))).T).all() > 0.001:
        new_A = a_plus_k(new_A, 1)
    return np.diag(new_A)


Q = macierzQ(A)

# R = np.round(np.dot(Q.T, A), decimals=5)
# xd = np.round(np.dot(Q, R), decimals=5)


print(Q)
print(A)
# print(xd)
# print(eo)
