def G(n):
    g = 1
    while n%2 == 0:
        g*=2
        n/=2
    return g

def modexp(a, b, M):
    if b == 0:
        return 1

    result = 1

    while b>0:
        if b%2:
            result = (result*a)%M

        b = b/2
        a = (a*a)%M

    return result

M = [None, 1]

def gcdmask(n):
    S = 0
    for X in [
        modexp(x, G(x), 998244353) for x in range(len(M), n+1)
                    ]:
        M.append((M[-1] + X)%998244353)
    return M[n]


for _ in range(input()):
    n = input()
    print gcdmask(n)
        
