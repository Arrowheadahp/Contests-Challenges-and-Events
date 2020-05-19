from collections import Counter

def modexp(a,b,c):
    # calculating a**b%c
    
    res = 1
    i=0
    while b>0:
        bit = b%2
        b = b/2
        res = (res * a**bit) % c
        a = (a*a)%c
        
    return res

def RE():
    return [int(i) for i in raw_input().split()]

for _ in range(input()):
    n = input()
    A = RE()
    
    C = Counter(A)
    i = 1
    d = 998244353
    N = modexp(2, n, d)
    S = N
    while C[i]!=0:
        n = n-C[i]
        S= (S+N-modexp(2, n, d))%d
        i+=1
        print S
        
    
