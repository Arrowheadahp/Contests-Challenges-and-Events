def RE():
    return [int(i) for i in raw_input().split()]

for _ in range(input()):
    n, s = RE()
    P = RE()
    T = RE()
    D = {0:float('inf'), 1:float('inf')}
    
    for t, p in zip(T, P):
        D[t] = min(D[t], p)
    if D[0]+D[1]<=100-s:
        print 'yes'
    else:
        print 'no'
        
