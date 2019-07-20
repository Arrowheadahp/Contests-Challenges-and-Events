RI=lambda : map(int,raw_input().split())

for _ in range(input()):
    n,m,k=RI()

    T=[[] for i in range(n+2)]

    f=0
    for i in range(k):
        
        t=RI()
        
        at= [[t[0]-1,t[1]],[t[0],t[1]-1],[t[0],t[1]+1],[t[0]+1,t[1]]]
        a=4
        for j in at:
            if j in T[j[0]]:
                a-=2
        f+= a
        
        T[t[0]].append(t)

    print f
