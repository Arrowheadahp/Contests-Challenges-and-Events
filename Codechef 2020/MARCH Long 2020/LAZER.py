def laz(L):
    #print L
    k = L[0]
    c = 0
    for i in L[1:]:
        c+= i!=k or i==0
        k=i
    return c
    

for _ in range(input()):
    n, q = map(int, raw_input().split())
    A = map(int, raw_input().split())

    for _ in range(q):
        x1, x2, y = map(int, raw_input().split())
        print laz([cmp(a, y) for a in A[x1-1:x2]])



'''
2
4 3
1 3 5 1
2 4 4
1 2 3
1 4 1
4 1
0 0 0 0
1 4 0
2 3 0
'''


