T=input()
P=[2]
for t in range(T):
    m,d,x=map(int,raw_input().split())
    lower=(x-1)*d+1
    upper=x*d
    c=0
    if P[-1]<upper:
        for j in range(P[-1]+1,upper+1):
            for k in P:
                if j%k==0:
                    break
            else:
                P.append(j)
        
    #print P
    for i in P:
        if i>=lower and i<=upper:
            c+=1

    #print c,d
    g,h=c,d
    r=d%c
    while r>0:
        d=c
        c=r
        r=d%c
    print g/c,h/c
