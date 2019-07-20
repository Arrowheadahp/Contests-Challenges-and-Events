def bir(n):
    t=int(n)
    r=[]
    while len(r)<30:
        r=[t%2]+r
        t/=2
    return list(r)

for _ in range(input()):
    n=input()
    A=map(bir,raw_input().split())

    #print A

    P=[0 for _ in range(30)]

    P=[sum([i[j] for i in A]) for j in range(30)]

    #P[::-1]
    
    for i in range(30):
        P[i]=min(P[i],n-P[i])

    s=0
    P=P[::-1]
    for i in range(30):
        s+=2**i*P[i]

    print s
        
        
    
