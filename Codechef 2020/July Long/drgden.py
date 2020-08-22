from collections import *
from math import *

def RE():
    return [int(i) for i in raw_input().split()]

def initialise():
    global M
    M = [[[] for _ in range(n)]for _ in range(n)]

    for start in range(n):
        
        # end<start
        S = [H[start]]
        Si = [start]
        end = start -1
        while end >=0:
            if len(S) == 0:
                break
            h = H[end]
            if h >= S[-1]:
                S.pop()
                Si.pop()
                continue

            S.append(h)
            Si.append(end)
            M[start][end] = list(Si)
            end-=1

        # end==start
        M[start][start] = [start]

        # end>start
        S = [H[start]]
        Si = [start]
        end = start +1
        while end < n:
            if len(S) == 0:
                break
            h = H[end]
            if h >= S[-1]:
                S.pop()
                Si.pop()
                continue

            S.append(h)
            Si.append(end)
            M[start][end] = list(Si)
            end-=1

##    for row in M:
##        for col in row:
##            print sum([A[a] for a in col]),
##        print
##    print
            
            

def func2():
    start = y-1
    end = z-1

    L = M[start][end]
    if len(L) == 0:
        print -1
    else:
        print sum([A[i] for i in L])
                


def func():
    start = y-1
    end = z-1

    d = cmp(end, start)
    if d == 0:
        print A[start]
        return
    
    L = [H[i] for i in range(start, end+d, d)]

##    print L
    
    S = [L[0]]
    Si = [0]
    i = 1
    while i<len(L):
        if len(S) == 0:
            print -1
            return 
        h = L[i]
        if h >= S[-1]:
            S.pop()
            Si.pop()
            continue

        S.append(h)
        Si.append(i)
        i+=1

##    print S
##    print Si

    taste = [A[start+d*i] for i in Si]
    
    print sum(taste)
        
            
        

def func1():
    global A
    A[y-1] = z


    
        
n, q = RE()
H = RE()
A = RE()
initialise()
for _ in range(q):
    x, y, z = RE()

    if x == 2:    
        func2()
    else:
        func1()

'''
5 5
3 1 4 1 5
1 2 4 8 16
2 5 2
1 3 5
2 3 4
2 1 4
2 5 5
'''
    
