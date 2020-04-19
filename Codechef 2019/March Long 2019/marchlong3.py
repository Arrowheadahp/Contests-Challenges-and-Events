t=int(raw_input().lstrip())
for i in range(t):
    n=input()
    r=0
    D=[{'a':0,'e':0,'i':0,'o':0,'u':0} for j in range(n)]
    for j in range(n):
        d=raw_input()
        for k in d:
            D[j][k]+=1
    for j in range(n-1):
        d=D[j]
        for k in D[j+1:]:
            for l in 'aeiou':
                if d[l]+k[l]==0:
                    break
            else:
                r+=1
    print r
