import math
import numpy as np

A = np.array([[1, 1], [0, 1], [-1, 1]])


def wartosci_wlasne(A):
    return np.round(np.linalg.eigvals(A), decimals=5)


def wektory_wlasne(A):
    return np.round(np.linalg.eig(A)[1], decimals=5)


def macierzV(A):
    X = np.dot(A.T, A)
    macierz_V = wektory_wlasne(X)
    wartosci = wartosci_wlasne(X)
    for i in range(len(wartosci)):
        wartosci[i] = math.sqrt(wartosci[i])
    sort = sorted(wartosci, reverse=True)
    return sort, macierz_V


def macierzU(A):
    X = np.dot(A, A.T)
    macierz_U = wektory_wlasne(X)
    wartosci = wartosci_wlasne(X)
    for i in range(len(wartosci)):
        wartosci[i] = math.sqrt(wartosci[i])
    sort = sorted(wartosci, reverse=True)
    return sort, macierz_U


def svd(A):
    if(len(A) > len(A[0])):
        m_V = np.ones((len(A[0]), len(A[0])))
        sig, m_U = macierzU(A)
        for i in range(len(sig)-1):
            m_V[i] = (np.dot(A.T, m_U[i])/sig[i])
        m_sig = np.zeros((len(A), len(A[0])))
        for i in range(len(sig)-1):
            for j in range(len(sig)-1):
                if i == j:
                    m_sig[i][j] = sig[i]

    elif(len(A) < len(A[0])):
        m_U = np.ones((len(A), len(A)))
        sig, m_V = macierzV(A)
        for i in range(len(sig)-1):
            m_U[i] = (np.dot(A, m_V[i])/sig[i])
        m_sig = np.zeros((len(A), len(A[0])))
        for i in range(len(sig)-1):
            for j in range(len(sig)-1):
                if i == j:
                    m_sig[i][j] = sig[i]

    print("Macierz U:")
    print(m_U)
    print("Macierz V:")
    print(m_V)
    print("Macierz Sigma:")
    print(m_sig)


svd(A)
svd(A.T)
