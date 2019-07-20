T=int(raw_input().lstrip())
for t in range(T):
    n=input()
    L=[]
    r=0
    for j in range(n):
        D={'a':0,'e':0,'i':0,'o':0,'u':0}
        d=raw_input()
        flag=0
        for k in d:
            D[k]=1
        for i in L:
            for v in 'aeiou':
                if i[0][v]+D[v]==0:
                    break
            else:
                r=r+i[1]
            if i[0]==D:
                i[1]+=1
                flag=1
        if flag==0:
            L.append([D,1])
    print r
