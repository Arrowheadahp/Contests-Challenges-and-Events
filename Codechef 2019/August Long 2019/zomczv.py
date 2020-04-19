from collections import Counter

for _ in range(input()):
    n = input()
    C = map(int, raw_input().split())
    H = map(int, raw_input().split())
    
    if max(H) > n:
        print 'NO'
        continue

    R = [0 for _ in range(n)]
    '''
    for i, c in enumerate(C):
        mx = max(i-c, 0)
        mn = min(i+c+1, n)
        R[mx: mn] = [j+1 for j in R[mx: mn]]
    print Counter(R),R
'''
    R1 = [[] for _ in range(n)]
    for i, c in enumerate(C):
        mx = max(i-c, 0)
        mn = min(i+c+1, n)
        R1[mx].append(2*c+1)


    
    '''#print R1
    R = [0 for _ in range(n)]
    X = []
    for i,r in enumerate(R1):
        X = [X[j]-1 for j in range(len(X)) if X[j]]
        X += r
        R[i]+=len(X)
        print X,'\t',R
    print Counter(R)'''

    if Counter(R) == Counter(H):
        print 'YES'

    else:
        print 'NO'
