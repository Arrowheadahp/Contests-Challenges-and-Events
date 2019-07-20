def hcf(x,y):
    a,b=x,y
    while a%b:
        a,b=b,a%b
    return b


for _ in range(input()):

    n=input()
    Tree={}
    
    for _ in range(n-1):
        u,v=map(int,raw_input().split())
        if u in Tree:
            Tree[min(u,v)].append(max(u,v))
        else:
            Tree[min(u,v)]=[max(u,v)]

    V=map(long,raw_input().split())
    M=map(long,raw_input().split())

    H={1:V[0]}
    branch=[1]

    print Tree
    
    while True:
        leaf=[]
        for i in branch:
            if i in Tree:
                for j in Tree[i]:
                    leaf.append(j)
                    H[j]=hcf(V[i-1],V[j-1])
        #print leaf
        if len(leaf)==0:
            break
        else:
            branch=list(leaf)

    branch.sort()
    print branch
    for l in branch:
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
