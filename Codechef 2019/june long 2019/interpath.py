def RI():
    return map(int,raw_input().split())

def bfsp(u,v):
    global T
    nbor=T[u]
    Qu=[]
    Qv=[]
    
    while True:
        if 
    





for _ in xrange(input()):
    n,q=RI()
    T={}
    for _ in xrange(n-1):
        p=RI()
        for v in [0,1]:
            if p[v] in T:
                T[p[v]].add(p[v-1])
            else:
                T[p[v]]=set(p[v-1])

    for _ in xrange(q-1):
        u,v=RI()
        P=bfsp(u,v)

            
                    
                    
            
            
