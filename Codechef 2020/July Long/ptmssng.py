from collections import *

def RE():
    return [int(i) for i in raw_input().split()]

def func():
    X = [x for x, y in P]
    Y = [y for x, y in P]

    X = Counter(X)
    Y = Counter(Y)

    ox = []
    for x in X:
        if X[x]%2:
            ox.append(x)
            print x,
            break

    oy = []
    for y in Y:
        if Y[y]%2:
            oy.append(y)
            print y
            break

##    print ox, oy
        
    
        

for _ in range(input()):
    n = input()
    P = [RE() for _ in range(4*n-1)]
    
    
    func()

    
