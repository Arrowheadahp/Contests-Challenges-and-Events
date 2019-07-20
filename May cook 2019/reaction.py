for _ in xrange(input()):
    r,c=map(int,raw_input().split())
    G=[]
    flag=0
    
    for i in xrange(r):
        R=map(int,raw_input().split())
        if flag==0:
            for j,b in enumerate(R):
                if b >3:
                    flag+=1
                    break
                if i==0 or i==r-1:
                    if b>=3:
                        flag+=1
                        break
                    if j==0 or j==c-1:
                        if b>=2:
                            flag+=1
                            break

    if flag==0:
        print 'Stable'

    else:
        print 'Unstable'

    
        
