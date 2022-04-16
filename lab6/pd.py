from unittest import result
import numpy as np
import math

A = [[1, 1, 0], [0, 1, 1]]


def kreseczki(vector):
    result = 0
    for i in range(len(vector)):
        result += vector[i]**2
    return math.sqrt(result)


def projekcja(u, v):
    # u = np.array(u)
    # v = np.array(v)
    l = np.dot(v, u)
    m = np.dot(u, u)
    return (l/m)*u


def upo(A):
    Q = []
    u1 = np.array(A[0])
    e1 = u1/kreseczki(u1)
    Q.append(e1)
    v2 = np.array(A[1])
    u2 = v2 - projekcja(u1, v2)
    e2 = u2/kreseczki(u2)
    Q.append(e2)
    return np.array(Q)


# print(kreseczki(A[0]))
# print(projekcja(A[0], A[1]))

Q = upo(A)
R = np.dot(Q, A)
xd = np.dot(Q, R)

print(A)
print(Q)
print(R)
print(xd)
