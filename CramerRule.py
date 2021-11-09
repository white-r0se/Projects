import numpy as np
from sympy import *

def CramerRule(A, b):
    n = len(A)
    det = np.linalg.det(A)
    x = []
    for i in range(n):
        Anew = A.copy()
        for j in range(n):
            Anew[j][i] = b[j][0]
        print(Anew)
        deti = np.linalg.det(Anew)
        x.append(round(deti/det, 3))
    return x


# A = np.array([
#     [1, 2, 3],
#     [1, 4, 9],
#     [1, 8, 27]
# ])
# b = np.array([
#     [4, 16, 46]
# ]).reshape((3, 1))
# print(CramerRule(A, b))

A = np.array([
    [6, 7, 6],
    [4, 8, 4],
    [4, 4, 3]
])
b = np.array([
    [315, 280, 194]
]).reshape((3, 1))
print(CramerRule(A, b))