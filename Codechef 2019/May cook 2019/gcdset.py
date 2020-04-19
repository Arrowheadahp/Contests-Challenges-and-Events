for _ in xrange(input()):
    l,r,g=map(int,raw_input().split())
    
    if l%g>0:
        lt=(l/g+1)
    else:lt=l/g
    rt=(r/g)

    a=rt-lt+1

    if a==1:
        if rt==1:
            print a
        else:
            print 0
    else:
        print a
