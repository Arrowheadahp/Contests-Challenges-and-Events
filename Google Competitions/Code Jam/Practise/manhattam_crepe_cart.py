def RE():
    return [int(i) for i in raw_input().split()]


def crepe():
    p, q = RE()
    
    lat = [[0,0] for _ in range(q+1)]
    lon = [[0,0] for _ in range(q+1)]
    M = [lon, lat]
    D = {'N':(1, 0),
         'S':(1, 1),
         'E':(0, 0),
         'W':(0, 1)}

    for _ in range(p):
        i, j, d = raw_input().split()
        p = [int(i), int(j)]
        h = D[d]
        M[h[0]] [p[h[0]]] [h[1]] += 1

    N = []
    for K in M:
        x, y = [], []
        s = 0
        for a, b in K:
            x.append(s)
            s+=a

        s = 0
        for a, b in K[::-1]:
            y.append(s)
            s+=b
        y = y[::-1]
        L = [x[i]+y[i] for i in range(q+1)]
        N.append(L)

    N = [L.index(max(L)) for L in N]
            
            
    return N


for t in range(input()):
    x, y = crepe()
    print 'Case #%d:'%(t+1), x, y
    
'''
4
1 10
5 5 N
4 10
2 4 N
2 6 S
1 5 E
3 5 W
8 10
0 2 S
0 3 N
0 3 N
0 4 N
0 5 S
0 5 S
0 8 S
1 5 W
4 10
6 10 S
6 8 N
8 8 E
10 10 W
'''
