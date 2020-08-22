from collections import *

def RE():
    return [int(i) for i in raw_input().split()]

def func():
    s = 0
    for p in range(1, n):
        if S[p] != S[p-1]:
            s+= abs(S[p]-S[p-1])-1

    print s
        

for _ in range(input()):
    n = input()
    S = RE()
    
    
    func()

    
