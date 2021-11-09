import numpy as np
from sympy import *
import matplotlib.pyplot as plt
import math

def C(k, n):
    return math.factorial(n)//(math.factorial(k) * math.factorial(n-k))


n = 100
A = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if j <= i:
            A[i][j] = C(j+1, i+1) % 2
colordic = {1: [0, 70, 153], 0: [253, 204, 100]}
n = [[colordic[i] for i in j] for j in A]
plt.imshow(n)
plt.show()
