for _ in range(input()):
    n,x=map(int,raw_input().split())
    A=map(int,raw_input().split())
    Edge=[]
    Tree={}
    
    for _ in range(n-1):
        '''Edge.append(map(int,raw_input().split()))'''

        u,v=map(int,raw_input().split())
        if u in Tree:
            Tree[u].append(v)
        else:
            Tree[u]=[v]


    branch=[1]
    while len(branch)>0:
        leaf=[]
        for i in branch:
            if i in Tree:
                for j in Tree[i]:
                    leaf.append(j)
                    Edge.append([i,j])
        branch=list(leaf)

    
    Edge=Edge[::-1]    

    for u,v in Edge:
        A[u-1]=A[u-1]+max(0-x,A[v-1])
        #print A

    print max(0-x,A[0])

