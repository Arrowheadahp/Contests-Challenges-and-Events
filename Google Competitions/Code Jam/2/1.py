def RE():
    return [int(i) for i in raw_input().split()]

def sree(diff):
    return (int((1+8*diff)**0.5)-1)/2

def func():
    K = RE()
    mx = K.index(max(K))
    mn = K.index(min(K))
    diff = K[mx] - K[mn]
    
    x = sree(diff)

    K[mx] -= (x*(x+1))/2

    if max(K) < x+1:
        return x, K[0], K[1]


    if K[1]>K[0]:
        x = x+1
        K[1] -= x

    t = (int((x*x+4*K[0])**0.5) -x)/2

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
    print ('Case #%d: %d %d %d' %(q+1, n, l, r))
