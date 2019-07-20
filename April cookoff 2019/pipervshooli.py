for _ in range(input()):
    n,a,b,x,y,z=map(int,raw_input().split())
    C=map(int,raw_input().split())

    days=(z-b)/y
    if (z-b)%y==0:
        days-=1
    req=z-(a+days*x)

    #print days,req
    
    con=0
    i=0
    C.sort(reverse=True)
    while req>0:
        #print C
        c=C[i]
        if c==0:
            print 'RIP'
            break
        req-=c
        con+=1

        #print req
        
        C[i]/=2
        i+=1
        if i==n:
            i=0

    else:
        print con
        
