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

def factlist(n):
    F = [1 for i in range(n+1)]
    f = 1
    for i in range(1, n+1):
        f*= i
        F[i] = f
    return F

def fact(n):
    f = 1
    for i in range(1, n+1):
        f*= i
    return f

l = 10**4
F = factlist(l+1)
for _ in range(input()):
    n = input()
    L = map(int, raw_input().split())

    s = 1.0*sum(L)/(n+1)

    
    R = Counter(L)
    if R[s]< 2:
        print 0
        continue
    s = int(s)
    
    R.subtract(Counter({s:2}))
    #print R
    tv = 1
    K = []
    for i in R:
        if R[i] != R[s-i]:
            print 0
            tv = 0
            break
        else:
            if i*2 == s:
                K.append(R[i]/2)
                K.append(R[i]/2)
            else:
                K.append(R[i])
    if tv == 0:
        continue



    
    #F = factlist(n)
    den = 1
    K = Counter(K)
    for i in K:
        if i <=l:
            den*=F[i]**(K[i]/2)
        else:
            den*=fact(i)
    print (modexp(2, n-1 - R[1.0*s/2]/2, 10**9+7)*fact(n-1)/den)%(10**9+7)
    
