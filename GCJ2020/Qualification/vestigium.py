for x in range(int(input())):
    m = int(input())
    M = [ [int(i) for i in raw_input().split()] for _ in range(m)]
    
    c = 0
    for i in range(m):
        S = set()
        for j in range(m):
            S.add(M[j][i])
        c+= len(S) < m

    k = sum([M[i][i] for i in range(m)])
    r = sum([ len(set(row))<m for row in M])
    print ('Case #%d: %d %d %d'%(x+1, k, r, c))
