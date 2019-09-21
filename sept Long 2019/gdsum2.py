from collections import Counter

n, k = map(int, raw_input().split())
A = map(int, raw_input().split())


C = Counter(A)
L = C.values()

print L
print

M = list(L)

X = 1+n
for i in range(k-1):
    s = sum(M)
    for j in range(len(M)):
        s -= M[j]
        M[j] = s
    print M
    for j in range(len(L)-1-i):
        t = L[j]*M[j]
        X = (X+t)%(10**9+7)
        #M[j-1] = t

print X
        
