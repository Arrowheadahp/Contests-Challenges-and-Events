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

def primality(n):
    if n < 2:
        return False
    for i in range(2,min(n, 10)):
        rem = modexp(i, n-1, n)
        if rem!=1:
            return False
    return True

for i in range(10**3):
    if primality(i):
        print i,',', 
