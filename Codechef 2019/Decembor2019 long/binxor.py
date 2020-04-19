def fact(n):
    f = 1
    for i in range(1,n+1):
        f*=i
    return f

def comb(n, r):
    s = min(r, n-r)
    b = max(r, n-r)

    rf = fact(s)
    tf = rf
    for i in range(s+1, b+1):
        tf *= i
    
    nf = tf
    for i in range(b+1, n+1):
        nf *= i
    
    return (nf/(rf*tf))





N = 10**5+1
  
factorialNumInverse = [0 for _ in range(N+1)]
naturalNumInverse = [0 for _ in range(N+1)]
fact = [0 for _ in range(N+1)]
  
def InverseofNumber(p): 
    naturalNumInverse[0] = naturalNumInverse[1] = 1
    for i in range(2, N + 1, 1): 
        naturalNumInverse[i] = (naturalNumInverse[p % i] * 
                                   (p - int(p / i)) % p) 
  
def InverseofFactorial(p): 
    factorialNumInverse[0] = factorialNumInverse[1] = 1
  
    for i in range(2, N + 1, 1): 
        factorialNumInverse[i] = (naturalNumInverse[i] * 
                                  factorialNumInverse[i - 1]) % p 
  
def factorial(p): 
    fact[0] = 1
  
    for i in range(1, N + 1): 
        fact[i] = (fact[i - 1] * i) % p 
  
def Binomial(N, R, p): 
      
    ans = ((fact[N] * factorialNumInverse[R])% p * 
                      factorialNumInverse[N - R])% p 
    return ans 
  




def summ2(n, s, e):
    C = comb(n, s)
    res = C
    for r in range(s, e, 2):
        C = (C *(n-r)*(n-r-1))/((r+1)*(r+2))
        res += C
    return res%(10**9+7)

def summ(n, s, e):
    res = 0
    for i in range(s, e+1,2):
        res += Binomial(n, i, 10**9+7)
    return res%(10**9+7)

p = 1000000007
InverseofNumber(p) 
InverseofFactorial(p) 
factorial(p) 


for _ in range(input()):
    n = input()
    a = raw_input().count('1')
    b = raw_input().count('1')
    
    s = abs(a-b)
    e = min(a+b, 2*n -a-b)
    
    print summ(n, s, e)


