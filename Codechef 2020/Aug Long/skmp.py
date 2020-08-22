from collections import *
from math import *

def RE():
    return [int(i) for i in raw_input().split()]

def func():
    c = dict(Counter(s) - Counter(p))
    
    l = [a for a in c for _ in range(c[a])]

    l.sort()
    M = ['', p[0], '']
    for a in l:
        i = cmp(a, p[0])
        M[i+1]+=a


    M.append(p)
    n = ''
    for d in sorted(M):
        if d and d[0] == p[0] and d!= p:
            d = d[1:]
        n+= d
    print n
    
        

for _ in range(input()):
    s = raw_input()
    p = raw_input()
    
    
    func()

    
