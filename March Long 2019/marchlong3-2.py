T=int(raw_input().lstrip())
for t in range(T):
    n=input()
    L=[]
    r=0
    for j in range(n):
        D={'a':0,'e':0,'i':0,'o':0,'u':0}
        d=raw_input()
        for k in d:
            D[k]=1
        for i in L:
            if i[0]==D:
                i[1]+=1
                break
        else:
            L.append([D,1])
    #print L
    for j in range(len(L)):
        d=L[j][0]
        for v in 'aeiou':
            if d[v]==0:
                break
        else:
            r=r+L[j][1]*(L[j][1]-1)/2
        for k in L[j+1:]:
            for l in 'aeiou':
                if d[l]+k[0][l]==0:
                    break
            else:
                r+=L[j][1]*k[1]
        #print r
    print r
