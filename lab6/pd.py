from unittest import result
import numpy as np
import math

A = np.array([[1, 0], [1, 1], [0, 1]])
# A = np.array(A)


def kreseczki(vector):
    result = 0
    for i in range(len(vector)):
        result += vector[i]**2
    return math.sqrt(result)


def projekcja(u, v):
    l = np.dot(v.T, u)
    m = np.dot(u.T, u)
    return (l/m)*u


def upo(A):
    Q = []
    v1 = []
    v2 = []
    for i in range(len(A)):
        v1.append(A[i][0])
        v2.append(A[i][1])
    u1 = np.array(v1)
    v2 = np.array(v2)
    e1 = u1/kreseczki(u1)
    Q.append(e1)
    u2 = v2 - projekcja(u1, v2)
    e2 = u2/kreseczki(u2)
    Q.append(e2)
    Q = np.array(Q)
    return np.array(Q.T)


# print(kreseczki(A[0]))
# print(projekcja(A[0], A[1]))
Q = upo(A)
R = np.dot(Q.T, A)
xd = np.dot(Q, R)

print(A)
print(Q)
print(R)
print("nsdjnsjnfknskd")
print(xd)
