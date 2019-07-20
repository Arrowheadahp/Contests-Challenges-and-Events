for _ in xrange(input()):
    n,m,k=map(int,raw_input().split())

    for x in [n,m]:
        nset=set([0])
        r=0
        for i in xrange(x):
            r=(r+k)%x
            nset.add(r)

        if len(nset) != x:
            print -1
            break

    else:
        print m*n

