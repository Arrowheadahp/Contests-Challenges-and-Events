from collections import *
from math import *

def RE():
    return [int(i) for i in raw_input().split()]

def proc(a, x):
    r = ceil(log(ceil(a*1.0/x), 2))
    return int(r) if r>1 else 1


def func():
    if len(set(A)) == 1:
        sub1()
        return

    G = sorted([a for a in A if a>=ceil(x*1.0/2)])
    
##    print G,
    if len(G) == 0:
        print len(A)
        return 

    s = proc(G[0], x) + (1 if G[0] > x else 0)
    for i in range(1, len(G)):
##        print s,
        s+= proc(G[i], G[i-1])

##    print s,

    l = len(A) - len(G)

    print int(s+l)
    

    



        
        

def sub1():
    a = A[0]
    t = ceil(a*1.0/x)
    l = ceil(log(t, 2))
    print int(l+n)
    


        

for _ in range(input()):
    n, x = RE()
    A = RE()
    
    
    func()

'''
9
4 10
1 2 3 4
10 5
1 2 3 4 5 6 7 8 9 10
5 25
100 100 100 100 100
5 24
50 100 100 100 100
5 10
8 16 16 16 16
5 10
1 8 10 16 110
5 5
1 2 3 4 5
5 1
40 30 20 10 50
3 10
20 1 110
'''
