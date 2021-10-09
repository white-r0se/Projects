import numpy as np
from sympy import *
import matplotlib.pyplot as plt
import math
from itertools import *
from scipy.special import factorial

def C(k, n):
    res = factorial(n)/(factorial(k) * factorial(n-k))
    return res


n = 70
A = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if j <= i:
            A[i][j] = C(j+1, i+1) % 2
            A[i][j] = np.around(A[i][j])
            if A[i][j] == 2:
                A[i][j] = 1
np.around(A)
print(A)
colordic = {1: [0, 70, 153], 0: [253, 204, 100]}
n = [[colordic[i] for i in j] for j in A]
plt.imshow(n)
plt.show()