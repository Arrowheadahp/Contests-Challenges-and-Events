T=int(raw_input().lstrip())
for t in range(T):
    n,K=map(int,raw_input().split())
    A=raw_input().split()
    for i in range(n):
        A[i]=int(A[i])
        
    r=0
    for i in range(n):
        S=[]
        for j in range(i,n):
            l=len(S)
            p=0
            if l>0:
                while p<l and S[p]<A[j]:
                    p+=1
            S.insert(p,A[j])
            k=K%(j-i+1)
            x=S[k-1]
            nx=0
            for h in S:
                if h==x:
                    nx+=1
            if nx in S:
                r+=1
    print r

            
