from collections import *
from math import *

def RE():
    return [int(i) for i in raw_input().split()]

def func(A):
    k = len(A)
    C = [cmp(A[i+1], A[i]) for i in range(k-1)]

    s = 0
    count = 0
    for a in C:
        if a==0:
            continue
        elif s>=0 and a>0:
            s+=a
        elif s<=0 and a<0:
            s+=a
        else:
            s = a
        
        if s>3 or s<-3:
            count+=1
            s = 0

    return count

    
    return 0

##T = [1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 4, 5, 5, 4, 3]
##print func(T)

for q in range(input()):
    k = input()
    A = RE()

    
    x = func(A)
    print ('Case #%d: %d' %(q+1, x))
