import numpy as np
from sympy import *
import matplotlib.pyplot as plt
import math

def ToList(H):
    res = [[0 for i in range(len(H))] for j in range(len(H))]
    for i in range(len(H)):
        for j in range(len(H[i])):
            res[i][j] = H[i][j]
    return res

H2 = np.matrix([[1, 1], [1, -1]]) 
import math
def adamar(n):
    k = math.log(n, 2) - 1
    if n == 1:
        return 1
    if n == 2:
        return H2
    else:
        return np.kron(H2, adamar(2**(k)))
H = adamar(2**6)
H = np.array(H)
H = ToList(H)
H.sort(reverse=True)
colordic = {-1: [20, 100, 200], 1: [250, 100, 27]}
n = [[colordic[i] for i in j] for j in H]
plt.imshow(n)
plt.show()