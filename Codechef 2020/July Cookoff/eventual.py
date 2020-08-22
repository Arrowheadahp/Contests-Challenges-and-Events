from collections import *
from math import *

def RE():
    return [int(i) for i in raw_input().split()]

def func():
    C = Counter(s)
    for c, f in C.items():
        if f%2 == 1:
            print 'NO'
            return

    print 'YES'
    return
        
    
        

for _ in range(input()):
    n = input()
    s = raw_input()
    
    func()

    
