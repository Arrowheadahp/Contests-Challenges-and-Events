from collections import *
from math import *

def RE():
    return [int(i) for i in raw_input().split()]

def fpl(n):
    return int(ceil(n*1.0/9))

def func():
    pcl = fpl(pc)
    prl = fpl(pr)

    print int(prl<=pcl), min(prl, pcl)
        
    
        

for _ in range(input()):
    pc, pr = RE()
    
    func()

    
