from collections import *
from math import *

def RE():
    return [int(i) for i in raw_input().split()]

def func(n, V):
    V = V + [-1]
    
    mx = -float('inf')
    count = 0
    for i in range(n):
        v = V[i]
        t = V[i+1]

        if v>mx and v>t:
            count+=1

        mx = max(mx, v)

    return count

    
    return 0

for q in range(input()):
    n = input()
    V = RE()

    
    x = func(n, V)
    print ('Case #%d: %d' %(q+1, x))
