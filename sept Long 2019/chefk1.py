for _ in range(input()):
    n, m = [int(i) for i in raw_input().split()]
    if m < n-1 or m > (n*(n+1))/2:
        print -1

    elif n<=2 and m<=1:
        print m

    elif m <= n+1:
        print 2

    elif m <= 2*n:
        print 3

    else:
        d = m/n
        r = m%n

        if r==0:
            print d*2-1
        elif r<=n/2:
            print d*2
        else:
            print d*2+1
