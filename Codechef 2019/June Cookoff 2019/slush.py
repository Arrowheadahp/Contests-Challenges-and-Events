# cook your code here
def RI():
    return map(int,raw_input().split())

for _ in xrange(input()):
    n,m=RI()
    C=RI()

    profit=0
    seq=[]
    for _ in range(n):
        d,f,b=RI()
        if C[d-1]>0:
            C[d-1]-=1
            profit+=f
            seq.append(d)
            
        else:
            profit+=b
            seq.append('x')

    L=[]
    for i in range(m):
        L+=[[i+1,C[i]]]
 
    for i in range(n):
        if seq[i]=='x':
            for j in range(len(L)):
                if L[j][1]>0:
                    seq[i]=L[j][0]
                    L[j][1]-=1
                    break

    print profit
    for i in seq:
        print i,
    print
            
