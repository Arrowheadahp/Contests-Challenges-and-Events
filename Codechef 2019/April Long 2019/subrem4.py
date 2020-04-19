def profit(pre,node):
    global Tree
    global A
    global x

    if node not in Tree:
        return max(A[node-1],0-x)

    elif node!=1 and len(Tree[node])==1:
        #print node,max(A[node-1],0-x)
        return max(A[node-1],0-x)
    
    else:
        s=A[node-1]
        for j in Tree[node]:
            if j!=pre:
                s+=profit(node,j)
        #print node,max(s,0-x)
        return max(s,0-x)


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
        if v in Tree:
            Tree[v].append(u)
        else:
            Tree[v]=[u]

    #print Tree
    p=profit(0,1)
    print p


'''
4
3 5
1 -5 -10
1 2
2 3
7 5
1 -5 -10 -2 -6 2 -10
1 2
2 3
2 4
2 5
1 6
3 7
1 5
3
1 5
-7
'''
