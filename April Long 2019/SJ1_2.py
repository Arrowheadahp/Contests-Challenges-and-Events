def hcf(x,y):
    a,b=x,y
    while a%b!=0:
        a,b=b,a%b
    return b


for _ in range(input()):

    n=input()
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

    V=map(long,raw_input().split())
    M=map(long,raw_input().split())

    H={1:V[0]}

    branch=[1]
    burned=[0]
    
    while len(branch)>0:
        leaf=[]
        for node in branch:
            desc=[y for y in Tree[node] if y not in burned]
            for l in desc:
                leaf.append(l)
                H[l]=hcf(V[node-1],V[l-1])

        burned,branch=list(branch),list(leaf)

    burned.sort()
    for l in burned:
        print M[l-1]-hcf(H[l],M[l-1]),
    print
            
            
            
'''
2
5
1 2
2 5
3 1
4 3
2 3 4 6 7
1 2 3 2 10
5
1 2
2 5
1 3
3 4
2 3 4 6 7
1 2 3 2 10
'''
