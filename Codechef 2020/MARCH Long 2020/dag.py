for _ in range(input()):
    n, k = map(int, raw_input().split())

    #SL = [set() for _ in range(n)]
    '''M = [[] for _ in range(n)]
    for i in range(k):
        T = map(int, raw_input().split())
        for j,v in enumerate(T):
            #SL[j].add(v)
            M[v-1].append(j)
    M = [[min(x), max(x)] for x in M]
    print M
    
    T = [[0 for _ in range(n)] for _ in range(n)]
    for i, x in enumerate(M):
        for j in range(x[0], x[1]+1):
            T[j][i] = 1

    for y in T:
        print y
    '''

    V = [0 for _ in range(n)]
    
    T = map(int, raw_input().split())
    for i in range(n-1):
        t = T[i]-1
        if V[t] == 0:
            V[t] = T[i+1]

    print V
    for _ in range(k-1):
        T = map(int, raw_input().split())
        S = set()
        for i in range(n-1):
            t = T[i]
            S.add(t)
            while V[t-1] in S:
                t = V[t-1]
            V[T[i]-1] = V[t-1]
        print V
            



'''
1
5 6
1 2 3 4 5
1 2 4 3 5
1 3 2 4 5
2 1 4 3 5
2 1 3 4 5
2 4 1 3 5
'''
