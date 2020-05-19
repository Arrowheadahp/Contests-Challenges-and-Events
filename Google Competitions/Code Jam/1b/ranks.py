def func(R, S):
    global x, L
    if 1 in [R, S]:
        return True
    for t in range(1, S):
        x.append([R, R*S-t -R])
##        i, j = x[-1]
##        A = L[:i]
##        B = L[i:i+j]
##        C = L[i+j:]
##        L = B+A+C
##    print L
    func(R-1, S)
    
    
def func2(R, S):
    L = [i for j in range(S) for i in range(R)]
##    print
##    print L
    while L[:S] != [0]*S:
##        bl = len(L) - L[::-1].index(L[0])
####        print bl
##        if bl == len(L):
##            bs = L.index(0)
##        else:
##            bs = L.index(L[bl])+1
        K = list(L[::-1])
        bl = K[1:].index(K[-1])
        nex = K[bl]
        try:
            bs = K[bl+1:].index(nex)
            
            
            i = len(L)-bl-bs-1
            j = bs
        except:
            i = L.index(0)
            j = len(L)
        x.append((i, j))
        A = L[:i]
        B = L[i:i+j]
        C = L[i+j:]
        L = B+A+C
##        print i, j, L
    






    

for q in range(input()):
    x = []
    R, S = [int(i) for i in raw_input().split()]
    
    L = [i for j in range(S) for i in range(R)]
##    print L
    
    func2(R, S)

    print 'Case #%d:'%(q+1), len(x)
    for i, j in x:
        print i, j
