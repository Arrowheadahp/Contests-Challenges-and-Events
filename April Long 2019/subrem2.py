def profit(node):
    global Tree
    global A
    global x

    if node not in Tree:
        print node,max(A[node-1],0-x)
        return max(A[node-1],0-x)
    
    else:
        s=0
        for j in Tree[node]:
            s+=profit(j)
        print node,max(A[node-1]+s,0-x)
        return max(A[node-1]+s,0-x)


for _ in range(input()):
    n,x=map(int,raw_input().split())
    A=map(int,raw_input().split())
    
    Tree={}
    
    for _ in range(n-1):
        u,v=map(int,raw_input().split())
        if u in Tree:
            Tree[u].append(v)
        else:
            Tree[u]=[v]

    print Tree

    print profit(1)
