from collections import *
from math import *

def RE():
    return [int(i) for i in raw_input().split()]

def func():
    md = -1
    for p in P:
        if k%p==0:
            md = max(md, p)

    print md
        
    
        

for _ in range(input()):
    n, k = RE()
    P = RE()
    
    func()

    
