from math import sqrt

def RE():
    return [long(i) for i in raw_input().split()]

def SA(b, c):
    D = b**2 + 4*c
    rD = int(sqrt(D))
    while rD**2 > D:
        rD-=1

    return (rD-b)/2

def func():
    K = RE()
    mx = K.index(max(K))
    mn = K.index(min(K))
    diff = K[mx] - K[mn]
    
##    x = (long(sqrt(1+8*diff))-1)/2
    x = SA(1, 2*diff)

    K[mx] -= (x*(x+1))/2

    if max(K) < x+1:
        return x, K[0], K[1]


    if K[1]>K[0]:
        x = x+1
        K[1] -= x

##    t = (long(sqrt(x*x+4*K[0])) -x)/2
    t = SA(x, K[0])

    K[0]-= (t*x+t*t)
    K[1]-= t*(t+x+1)

##    print K, x, t

    if K[1]>=0:
        return x+2*t, K[0], K[1]

    K[1] += x+2*t

    return x+2*t-1, K[0], K[1]

    
    return 0

for q in range(input()):
    n, l, r = func()
    print ('Case #%d:'%(q+1)), n, l, r
