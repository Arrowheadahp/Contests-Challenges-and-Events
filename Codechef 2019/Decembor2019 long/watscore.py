from collections import defaultdict

for _ in range(input()):
    n = input()
    D = defaultdict(int)
    for i in range(n):
        p, s = map(int, raw_input().split())
        D[p] = max(D[p], s)
    
    s = 0
    for p in range(1,9):
        s += D[p]
    
    print s
