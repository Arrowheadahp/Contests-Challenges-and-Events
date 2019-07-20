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
        u,v=min(u,v),max(u,v)
        if u in Tree:
            Tree[u].append(v)
        else:
            Tree[u]=[v]

    V=map(long,raw_input().split())
    M=map(long,raw_input().split())

    H={1:V[0]}
    branch=[1]
    end=[]

    #print Tree
    
    while branch:
        sub=[]
        for i in branch:
            if i in Tree:
                sub+=Tree[i]
                for j in Tree[i]:
                    H[j]=hcf(V[j-1],H[i])

            else:
                end.append(i)
        branch=list(sub)
        

    end.sort()
    #print end
    for l in end:
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
