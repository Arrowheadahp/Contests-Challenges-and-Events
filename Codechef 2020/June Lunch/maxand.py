from collections import *

def RE():
    return [int(i) for i in raw_input().split()]

def one(n):
    L = []
    s = bin(n)[2:]
    s = s[::-1]
    for i, c in enumerate(s):
        if c == '1':
            L.append(i)

    return L


def func():
    X = []
    for a in A:
        X += one(a)

    C = Counter(X)
    O = range(32)
    O.sort(key = lambda i: C[i]*2**i, reverse = True)
    O = set(O[:k])

    x = ''
    i = 0
    while i<32:
        if i in O:
            x = '1'+x
        else:
            x = '0'+x
        i+=1

    print int(x, 2)   
    
        

for _ in range(input()):
    n, k = RE()
    A = RE()

    func()

    
