for _ in range(input()):
    n, k = [int(i) for i in raw_input().split()]
    P = [int(i) for i in raw_input().split()]

    A = [0 for p in P]
    for i, p in enumerate(P):
        A[p-1] = i+1

    L = []
    for i in range(1, n+1):
        
##        print P
        
        p = P[i-1]

        if i == p:
            continue
        
        a = P[i:].index(i)+i+1 if P[A[i-1]-1]!=i else A[i-1]
        if p == a:
            if a-1!=i:
                p = a-1
            elif a == n:
                print -1
                break
            else:
                p = a+1
        
        L.append([i, p, a])
        P[i-1], P[p-1], P[a-1] = P[a-1], P[i-1], P[p-1]
        
        if len(L)>k:
            print -1
            break
    else:
        print len(L)
        for i, j, k in L:
            print i, j, k
'''
4
4 2
3 2 4 1
4 2
4 3 2 1
4 2
4 2 3 1
4 2
1 3 2 4
'''     
