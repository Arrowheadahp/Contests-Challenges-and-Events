from collections import *

def RE():
    return [int(i) for i in raw_input().split()]

def func():
    Ca = Counter(A)
    Cb = Counter(B)

    D = {a: Ca[a]-Cb[a] for a in set(A)|set(B)}

    P = []
    N = []

    m = min(min(A), min(B))

    for a in D:
        k = D[a]
        if k%2:
            return -1

        k/=2

        if k>0:
            P.append([a, k])
        if k<0:
            N.append([a, -k])

    P.sort(key = lambda t: t[0])
    N.sort(key = lambda t: t[0], reverse = True)

    return func3(P, N, m)

def func3(P, N, m):
    X = []
    for a, d in P:
        X+= [a]*d
    Y = []
    for a, d in N:
        Y+= [a]*d

    s = 0
    for i in range(len(X)):
        s+= min(X[i], Y[i], 2*m)

    return s


def func2(P, N):

    l = 0
    r = 0
    s = 0

    while l<len(P) and r<len(N):
        la, lk = P[l]
        ra, rk = N[r]

        if lk == 0:
            l+=1
            continue
        if rk == 0:
            r+=1
            continue

        ma = min(la, ra)
        mk = min(lk, rk)
        s+= ma*mk

        P[l][1]-=mk
        N[r][1]-=mk
        
    return s
        
    
        

for _ in range(input()):
    n = input()
    A = RE()
    B = RE()
    
    
    print func()

    
