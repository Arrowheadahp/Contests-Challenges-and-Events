from collections import *
from math import *

def RE():
    return [int(i) for i in raw_input().split()]

def func(A):
    if len(set(A)) != n:
        print 'NO'
        return
    M = [A, A[::-1]]
    for A in M:
        o = 0
        for a in A:
            p = o | a
##            print a, o, p
            if o==p and o!=0:
                print 'NO'
                return
            o = p
    print 'YES'
    
        

for _ in range(input()):
    n = input()
    A = RE()
    
    func(A)

    
