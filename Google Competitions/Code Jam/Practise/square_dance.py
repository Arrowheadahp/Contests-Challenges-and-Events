def RE():
    return [int(i) for i in raw_input().split()]

def comp(i, j):
    global r, c, M
##    X = [i+x for x in [-1,1] if 0<=i+x<len(grid)]
##    Y = [j+x for x in [-1,1] if 0<=j+x<len(grid[i])]
    P = []
    x = 1
    p = 0
    while 0<=i+x<r:
        p = M[i+x][j]
        if p:
            P.append(p)
            break
        x+=1

    x = -1
    p = 0
    while 0<=i+x<r:
        p = M[i+x][j]
        if p:
            P.append(p)
            break
        x-=1

    x = 1
    p = 0
    while 0<=j+x<c:
        p = M[i][j+x]
        if p:
            P.append(p)
            break
        x+=1

    x = -1
    p = 0
    while 0<=j+x<c:
        p = M[i][j+x]
        if p:
            P.append(p)
            break
        x-=1
    
    if len(P)==0:
        return 0

    avg = sum(P)*1.0/len(P)
    return avg
        
def roun():
    global r, c, M
    S = 0
    K = [[M[j][i] for i in range(c)]for j in range(r)]
    T = [[-1 for _ in range(c)]for _ in range(r)]
    for i in range(r):
        for j in range(c):
            S+=M[i][j]
            avg = comp(i, j)
            T[i][j] = avg
            if M[i][j]<avg:
                K[i][j] = 0
    M = K
##    print S
##    for m in T:
##        print m
##    print
##    for m in M:
##        print m
##    print
##    print
    return S


def func():
    S = 0
    p = 1
    t = 0
    while p!= t:
        p = t
        t = roun()
        S+=p
    return S
        



for q in range(input()):
    r, c = RE()
    M = [RE() for i in range(r)]
    il = func()
    print 'Case #%d: %d'%(q+1, il)
