def RE():
    return [int(i) for i in raw_input().split()]

def func():
    r, c = RE()
    C = [raw_input() for _ in range(r)]
    T = set()

    L = []

    for i in range(c):
        Str = ''
        Set = set()
        for j in range(r):
            
            k = C[r-j-1][i]
            T.add(k)
            if k in Set:
                if k!= Str[-1]:
                    return -1
            else:
                Set.add(k)
                Str+=k
        L.append(Str)


    D = defaultdict(set)
    for s in L:
        for i in range(len(s)-1):
            c = s[i+1]
            t = s[i]
            if c in D[t]:
                return -1
            D[c].add(t)

##    print D
    S = []
    ss = set()
    while len(S)<len(T):
        k = list(T)
        e = set(k)

        B = [x for x in D if len(D[x])>0]
##        print S

        d = e.difference(set(B))
##        print d
        for c in d:
            if c not in ss:
                S.append(c)
                ss.add(c)
                for f in D:
                    if c in D[f]:
                        D[f].remove(c)
##    print S
    R = ''
    for s in S:
        R+=s
    return R
                


    
    return 0

from collections import defaultdict
for q in range(input()):
    x = func()
    print ('Case #%d: %s' %(q+1, x))
