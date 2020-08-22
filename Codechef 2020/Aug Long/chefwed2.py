from collections import *
from math import *
inf = float('inf')

def RE():
    return [int(i) for i in raw_input().split()]


def conflict(L):
    C = Counter(L)
    s = 0
    for a, co in C.items():
        s += co if co>1 else 0
    return s

def func(l, r):
    if M[l][r]:
        return M[l][r]
    
    L = F[l: r]
    tc = [k+ conflict(L)]
    
    for i in range(l+1, r):
        tc.append(func(l, i) + func(i, r))

##    print tc
    M[l][r] = min(tc)
##    for col in M:
##        print col
    return min(tc)
    
##def func2(l, r):
##    L = F[l:r]
##    if M[l][r]:
##        return M[l][r]
##    if len(L) == 1:
##        return k
##    else:
##        return min(k+conflict(L), func2(l-1, r), func2(  

for _ in range(input()):
    n, k = RE()
    F = RE()
    M = [[None for _ in range(n+1)] for _ in range(n+1)]
    
    
    print func(0, n)

    
