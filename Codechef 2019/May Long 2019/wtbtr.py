for _ in xrange(input()):
    n=input()
    L1,L2=[],[]
    for _ in xrange(n):
        x,y=map(int,raw_input().split())
        
        L1.append(x+y)
        L2.append(x-y)

    L1.sort()
    L2.sort()

    mn=1000000000
    for i in xrange(n-1):
        mn=min(mn,L1[i+1]-L1[i],L2[i+1]-L2[i])

    print mn*1.0/2
    
    
        
