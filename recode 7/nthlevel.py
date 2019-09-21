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


for _ in range(input()):
    n, l = map(int, raw_input().split())

    print (l**2 * modexp(3, n-1, 10**9+7))%(10**9+7)
