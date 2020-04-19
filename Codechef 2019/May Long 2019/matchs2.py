for _ in xrange(input()):
    n,m=map(long,raw_input().split())

    a,b=max(m,n),min(m,n)

    t=0
    w='flag'
    while True:
        if a>b*2:
            w=t
        a,b=b,a%b

        if not b:
            break
        t=1-t

    if w=='flag':
        w=t

    if w==0:
        print 'Ari'
    else:
        print 'Rich'
        
'''
9
1 1
2 2
1 3
155 47
6 4
10 4
14 4
5 7
5 12
'''
