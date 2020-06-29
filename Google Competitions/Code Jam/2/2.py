def RE():
    return [int(i) for i in raw_input().split()]

from collections import defaultdict, deque

def func():
    c, d = RE()
    X = [0]+RE()

    CD = defaultdict(set)
    CL = []
    for _ in range(d):
        u, v = RE()
        CL.append((u, v))
        CD[u].add(v)
        CD[v].add(u)


    #BFS

    Q = deque()
    Q.append(1)
    S = set([1])

    T = [-1 for _ in range(c)]
    time = 0

    for i, x in enumerate(X):
        if x<=0:
            T[i] = -10000*x
##    print T
    
    while Q:
        n = Q.popleft()
        nex = CD[n]
        tn = T[n-1]
##        print n, tn
        for m in nex:
            if m not in S:
                S.add(m)
                Q.append(m)

                t = T[m-1]
                if t>0:
                    continue
                T[m-1] = tn+X[m-1]
##    print T
    L = []
    for conn in CL:
        u, v = conn
        L.append(abs(T[u-1]-T[v-1]))
    return L

                
def func2():
    c, d = RE()
    X = [0] + RE()

    L = []
    for _ in range(d):
        u, v = RE()
        L.append(abs(X[u-1]-X[v-1])*100)
    return L    
    return 0






def func3():
    c, d = RE()
    X = [0] + RE()

    T = [(x, i) for i, x in enumerate(X) if x>=0] + [(float('inf'), -1)]
    R = [(-x, i) for i, x in enumerate(X) if x<0] + [(c, -1)]

    T.sort(key = lambda x: x[0])
    R.sort(key = lambda x: x[0])

##    print T, R

    T.reverse()
    R.reverse()

    t = T.pop()
    r = R.pop()
    M = [-1 for _ in range(c+1)]
    n = 0
    time = 0
    

    while R:
        if r[0] > n:
            n+=1
            time = t[0]
            M[t[1]] = time
            t = T.pop()
        else:
            time += r[0]==n
            n+=1
            M[r[1]] = time
            r = R.pop()

##        print M, t, r

    M.pop()
##    print M
    
    L = []
    for _ in range(d):
        u, v = RE()
        L.append(abs(M[u-1]-M[v-1]))
    return L  
        
        
        






























for q in range(input()):
    x = func3()
    print ('Case #%d:' %(q+1)),
    for i in x:
        if not i:
            i = 300000
        print i,
    print
