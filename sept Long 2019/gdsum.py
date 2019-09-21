from collections import Counter

n, k = map(int, raw_input().split())
A = map(int, raw_input().split())


C = Counter(A)
x = 1
s = 0
for i in range(1, k+1):
    s = (s+x)%(10**9+7)
    x = (x*(n-i+1))/i
    #print i,(n-i+1)/i,x
print (s+x)%(10**9+7)

'''
4 2
1 2 3 4
'''
