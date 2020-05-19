for _ in range(input()):
    n, k = [int(i) for i in raw_input().split()]
    P = [int(i) for i in raw_input().split()]

    A = [0 for p in P]
    for i, p in enumerate(P):
        A[p-1] = i+1

    L = []
    for i in range(1, n+1):
        
##        print P
##        print A
##        print L
        
        p = P[i-1]
        a = A[i-1]
        if P[a-1] != i:
            a = P.index(i)+1
        if i==p:
            continue
        if p==a:
            x = i
            while x<n:
                if P[x]!=x+1 and P[x]!=i:
                    p = x+1
                    break
                x+=1
            else:
                print -1
                break

        L.append([i, p, a])
        P[i-1], P[p-1], P[a-1] = P[a-1], P[i-1], P[p-1]
        
        if len(L)>k:
            print -1
            break
    else:
        print len(L)
        for i, j, k in L:
            print i, j, k
##    print

'''
3
4 2
3 2 4 1
4 2
4 3 2 1
4 2
4 2 3 1
'''
            
