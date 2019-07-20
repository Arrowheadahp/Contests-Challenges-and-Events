from sys import stdin
RI = lambda : map(int, stdin.readline().split())

for _ in range(input()):
    n,m,k=RI()

    T=[]

    f=0
    for i in range(k):
        
        t=RI()
        
        at= [[t[0]-1,t[1]],[t[0],t[1]-1],[t[0],t[1]+1],[t[0]+1,t[1]]]
        a=4
        for j in at:
            if j in T:
                a-=2
        f+= a
        
        T.append(t)

    print f
    
        
        
    
