from collections import *
from math import *

def RE():
    return [int(i) for i in raw_input().split()]

def func(h, p):
    mh = 0
    while p:
        mh+= p
        p/=2
    print int(mh>=h)
        
        
    
        

for _ in range(input()):
    h, p = RE()
    
    func(h, p)

    
