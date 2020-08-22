from collections import *
from math import *
import sys
sys.setrecursionlimit(1000000)

def RE():
    return [int(i) for i in raw_input().split()]

def conflict(L):
    C = Counter()
    for d in L:
        C+= d
    s = 0
    for a, co in C.items():
        s += co if co>1 else 0
    return s


def gfunc(F, k):
    global T
    T = []

    t = Counter()
    for f in F:
        if f in t:
            T.append(t)
            t = Counter()
        t[f]+=1
    if len(t):
        T.append(t)

    l = len(T)
    global M
    M = [[None for _ in range(l+1)] for _ in range(l+1)]
    
    return func(0, l)


def func(l, r):
    if M[l][r]:
        return M[l][r]
    
    L = T[l: r]
    tc = [k+ conflict(L)]

    if tc[0] < 2*k:
        M[l][r] = min(tc)
        return min(tc)
    
    for i in range(l+1, r):
        tc.append(func(l, i) + func(i, r))

##    print tc
    M[l][r] = min(tc)
    return min(tc)
    



for _ in range(input()):
    n, k = RE()
    F = RE()
    
    
    print gfunc(F, k)

    
