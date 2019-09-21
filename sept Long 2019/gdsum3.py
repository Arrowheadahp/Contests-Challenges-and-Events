from collections import Counter

n, k = map(int, raw_input().split())
A = map(int, raw_input().split())

L = Counter(A).values()
M = list(L)
S = 1

for i in range(min(k,len(L))):
    x = sum(M)
    S = (S+x)%(10**9+7)

    for j in range(len(M)):
        x -= M[j]
        M[j] = x*L[j]
    print M
        
print S   
