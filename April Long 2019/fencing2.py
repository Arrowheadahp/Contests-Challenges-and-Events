RI=lambda : map(int,raw_input().split())

for _ in range(input()):
    n,m,k=RI()

    G=[ [0 for i in range(m+2)] for j in range(n+2)]

    f=0
    for i in range(k):
        r,c=RI()
        G[r][c]=1

        a=4
        for p in [[r-1,c],[r+1,c],[r,c-1],[r,c+1]]:
            if G[p[0]][p[1]]==1:
                a-=2
        
        f+=a
        '''for j in G:
            print j
        print f'''
    print f
