from collections import *

def RE():
    return [int(i) for i in raw_input().split()]

def digsum(n):
    s = 0
    for d in str(n):
        s+= int(d)

    return s

def func(R):
    R = [(digsum(a), digsum(b)) for a, b in R]
    W = [ cmp(a, b) for a, b in R ]

    A = W.count(1) + W.count(0)
    B = W.count(-1)+ W.count(0)

    if A == B:
        print 2, A
    elif A > B:
        print 0, A
    else:
        print 1, B

    
    
        

for _ in range(input()):
    n = input()
    R = [RE() for _ in range(n)]
    
    func(R)

    
