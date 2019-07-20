RI=lambda : map(int,raw_input().split())

for _ in range(input()):
    n,m,k=RI()

    P={}

    f=0
    for i in range(k):
        
        r,c=RI()
        a=4

        at=[[r-1,c],[r+1,c],[r,c-1],[r,c+1]]
        for x,y in at:
            if x in P and y in P[x]:
                a-=2
                
        f+=a



        if r in P:
            P[r].append(c)
        else:
            P[r]=[c]
        

    print f
