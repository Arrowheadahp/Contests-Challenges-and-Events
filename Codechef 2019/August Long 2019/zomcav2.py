from collections import Counter

for _ in range(input()):
    n = input()
    C = map(int, raw_input().split())
    H = map(int, raw_input().split())
    
    if max(H) > n:
        print 'NO'
        continue

    R = [0 for _ in range(n)]
    
    R1 = [[] for _ in range(n+1)]
    for i, c in enumerate(C):
        mx = max(i-c, 0)
        mn = min(i+c+1, n)
        R1[mx].append(i)
        R1[mn].append(i)
    S = set()
    for i in range(n):
        for j in R1[i]:
            if j in S:
                S.remove(j)
            else:
                S.add(j)
        R[i]+=len(S)
        

    if Counter(R) == Counter(H):
        print 'YES'

    else:
        print 'NO'
