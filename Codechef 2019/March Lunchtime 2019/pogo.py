T=input()
for t in range(T):
    n,k = map(int,raw_input().split())
    A=map(int,raw_input().split())

    n=len(A)
    m=0
    for i in range(-1,-1-k,-1):
        s=0
        #print i,'->'
        for j in range(i,-1*n-1,-k):
            s=s+A[j]
            m=max(m,s)
            #print j,s,m
    print m
