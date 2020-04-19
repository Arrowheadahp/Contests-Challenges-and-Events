def linput():
    return map(int, raw_input().split())


def dist(s, e):
    sx, sy = s[0], s[1]
    ex, ey = e[0], e[1]
    return(1.0*((ex-sx)**2+(ey-sy)**2))**0.5


def coord(L, i):
    return (L[i*2], L[i*2+1])


for _ in range(input()):
    x, y = linput()
    n, m, k = linput()

    N = linput()
    M = linput()
    K = linput()

    NMm = [[dist(coord(N, a), coord(M, b)) for a in range(n)] for b in range(m)]
    MNm = [ [ j[i] for j in NMm] for i in range(n)]
    NKd = [min(     [dist(coord(N, j), coord(K, i)) for i in range(k)]  ) for j in range(n)]
    MKd = [min(     [dist(coord(M, j), coord(K, i)) for i in range(k)]  ) for j in range(m)]
    
    L1 = [dist((x, y), coord(N, j))
          for j in range(n)]
    L2 = [dist((x, y), coord(M, j))
          for j in range(m)]
    #L = sorted(L1+L2, key=lambda t: t[1])

    NMl = [min([   i[j]+NKd[j]    for j in range(n)]) for i in NMm] #adding distance to k from n
    MNl = [min([   i[j]+MKd[j]    for j in range(m)]) for i in MNm] #adding distance to k from m

    print min(  [NMl[i] + L2[i]   for i in range(m)] + [MNl[i] + L1[i]   for i in range(n)]  )



'''
2
1 4
3 2 2
4 4 2 0 8 1
10 1 3 1
1 3 9 5
6 4
2 2 3
7 10 5 7
1 6 2 3
1 8 0 7 0 2
'''