from collections import *
from math import *

def RE():
    return [int(i) for i in raw_input().split()]

def conflict(C):
    s = 0
    for a, co in C.items():
        s += co if co>1 else 0
    return s


def func(F, k):
    T = []

    t = Counter()
    for f in F:
        if f in t:
            T.append(t)
            t = Counter()
        t[f]+=1
    if len(t):
        T.append(t)

##    print T
    return ineff(T)

    

def ineff(T):

    while len(T)>1:
        for i in range(len(T)-1):
            a, b = T[i], T[i+1]
            c = a + b
            if conflict(c)<=k+ conflict(a)+conflict(b):
                T[i:i+2] = [c]
                break
        else:
            break
    print T

    res =  len(T)*k + sum([conflict(a) for a in T])#    , '\n'
##    print res
    return res
    

for _ in range(input()):
    n, k = RE()
    F = RE()
    
    
    print func(F, k)

    
