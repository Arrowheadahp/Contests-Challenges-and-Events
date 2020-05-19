def RE():
    return [int(i) for i in raw_input().split()]

def func():
    n, k = RE()
    A = RE()

    count = 0

    i = 0
    while i<n:
        r = k
        while i<n and A[i] == r:
            if r==1:
                count +=1
                break
            r-=1
##            print 'in', i, A[i]
            i+=1
            
        if r==k:
##            print 'ot', i, A[i]
            i+=1

    return count

    
    return 0

for q in range(input()):
    x = func()
    print ('Case #%d: %d' %(q+1, x))
