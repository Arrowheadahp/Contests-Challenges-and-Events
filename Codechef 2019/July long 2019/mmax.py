for _ in xrange(input()):
    n=input()
    k=long(raw_input())

    r=k%n
    if r==1.0*n/2:
        print 2*r-1
    else:
        print 2*min(r,n-r)
