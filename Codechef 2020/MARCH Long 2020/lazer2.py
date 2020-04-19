from collections import defaultdict
for _ in range(input()):
    n, q = map(int, raw_input().split())
    A = map(int, raw_input().split())

    D = defaultdict(list)
    for i in range(n-1):
        a = min(A[i], A[i+1])
        b = max(A[i], A[i+1])
        for j in range(a, b+1):
            D[j].append(i+1)

    #print D

    for _ in range(q):
        x1, x2, y = map(int, raw_input().split())
        print len([a for a in D[y] if x1<=a<x2])
