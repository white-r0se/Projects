def Plac(n,m):
        z=1
        for i in range(0,m):
            z=z*(n-i)
        return z

A = [1, 5, 4]

def Func1(L, A, n, m):
    Free = [i+1 for i in range(n)]
    for i in range(1, m+1):
        t = Plac(n-i, m-i)
        q = L // t
        A[i-1] = Free[q]
        for j in range(q+1, n-i+1):
            Free[j-1] = Free[j]
        L = L % t
    return A
print(Func1(32, A, 5, 3))
# A = Func1(32, A)

def Func2(A, n, m):
    ws = []
    L = 0
    for i in range(1, m+1):
        num = 0
        for j in range(1, A[i-1]):
            if not(j in ws):
                num += 1
        ws = ws + [A[i-1]]
        L = L + num*Plac(n-i, m-i)
    return L
print(Func2(A, 5, 3))
