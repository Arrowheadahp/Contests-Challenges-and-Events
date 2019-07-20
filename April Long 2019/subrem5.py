for _ in range(input()):
    n,x=map(int,raw_input().split())
    A=map(int,raw_input().split())
    
    Tree={1:[0]}
    
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

    C=[]
    branch=[1]
    burned=[0]
    while branch:
        leaf=[]
        
        C+=[[node,y] for node in branch for y in Tree[node] if y not in burned]
        leaf+=[y for node in branch for y in Tree[node] if y not in burned]
        
        burned,branch=set(list(branch)),list(leaf)

    #print C
    C=C[::-1]

    for u,v in C:
        A[u-1]=A[u-1]+max(0-x,A[v-1])

    print max(0-x,A[0])


'''
4
3 5
1 -5 -10
1 2
2 3
7 5
1 -5 -10 -2 -6 2 -10
2 1
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
