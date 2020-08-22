from collections import *
from math import *

def RE():
    return [int(i) for i in raw_input().split()]

def substring(s):
    l = len(s)
    S = []
    for i in range(l+1):
        for j in range(i):
            S.append(s[j:i])

    return S

def D(s):
    S = substring(s)
    k = len(set(S)) - len([sb for sb in S if sb==sb[::-1]])
    print S
    return k

def sa(t):
    a = 1
    b = -1
    c = -2*t
    return int((-b + (b**2-4*a*c)**0.5)/(2*a))

def func():
    k = sa(d)
    m = (k*(k-1))/2

    print d, k, m
        
        
    
        

for _ in range(input()):
    d = input()
    
    func()
    print D(raw_input())

    
