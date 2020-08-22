from collections import *

def RE():
    return [int(i) for i in raw_input().split()]

def func(k):
    C = [['.']*8 for _ in range(8)]
    
    for i in range(8):
        for j in range(8):
            if 64-k>0:
                C[i][j] = 'X'
                k+=1

    C[-1][-1] = 'O'

    for r in C:
        s = ''
        for c in r:
            s+= c

        print s
        
        
    
        

for _ in range(input()):
    k = input()
    
    func(k)

    
