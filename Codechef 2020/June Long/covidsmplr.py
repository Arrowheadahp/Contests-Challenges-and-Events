from collections import *
import sys

def RE():
    return [int(i) for i in raw_input().split()]

def flushprint(L):
    for s in L:
        print s,
    print

    sys.stdout.flush()


def populate(T):
    M = [[0]*n for _ in range(n)]
    for r in range(n):
        prfs = 0
            
        for c in range(n):
            if r == 0:
                prvs = 0
            else:
                prvs = T[r-1][c]

            curr = T[r][c] - prvs - prfs

            prfs += curr
            M[r][c] = curr

    return M


    

def func():

    for r in range(n):
        for c in range(n):
            flushprint([1, 1, 1, r+1, c+1])
            fb = input()
            if fb == -1:
                return False
            T[r][c] = fb
            

def printmatrix(M):
    print 2
    for r in M:
        for rc in r:
            print rc,
        print

    sys.stdout.flush()


for _ in range(input()):
    n, p = RE()

    T = [[0]*n for _ in range(n)]

    verd = func()
    if verd == False:
        break

    M = populate(T)
    printmatrix(M)

    verd = input()
    if verd == -1:
        break
    
    
    
