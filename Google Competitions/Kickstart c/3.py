def RE():
    return [int(i) for i in raw_input().split()]

T = set([i**2 for i in range(10**4)])

def check(k):
    return k in T
    if k<0:
        return False
    return (int(k**0.5)**2)==k

def func():
    n = input()
    A = RE()

    PS = [0]
    s = 0
    for a in A:
        s+=a
        PS.append(s)

##    print PS

    K = [check(PS[i]-PS[j]) for i in range(n+1) for j in range(i)]
    return sum(K)

    count = 0
    for i in range(n+1):
        for j in range(i):
            k = PS[i]-PS[j]
##            print k
            if check(k):
                count+=1

    return count
        









    
    return 0

for q in range(input()):
    x = func()
    print ('Case #%d: %d' %(q+1, x))
