for _ in xrange(input()):
    r,c=map(int,raw_input().split())
    G=[]
    flag=0

    
    
    for i in xrange(r):
        R=map(int,raw_input().split())
        if flag==0:
            for j,b in enumerate(R):
                t=4
                if j==0:
                    t-=1
                if j==c-1:
                    t-=1
                if i==0:
                    t-=1
                if i==r-1:
                    t-=1

                if b>t:
                    flag=1
                    print b,t
                    break

    if flag==0:
        print 'Stable'

    else:
        print 'Unstable'

    
        
