import heapq
T=int(raw_input().lstrip())
for t in range(T):
    n,K=map(int,raw_input().split())
    A=raw_input().split()
    for i in range(n):
        A[i]=int(A[i])
        
    r=0
    for i in range(n):
        #trying heap here
        S=[]
        for j in range(i,n):
            heapq.heappush(S,A[j])
            k=K%(j-i+1)
            if k==0:
                x=heapq.nlargest(1,S)[-1]
            else:
                x=heapq.nsmallest(k,S)[-1]

            nx=0
            for h in S:
                if h==x:
                    nx+=1
            if nx in S:
                r+=1
    print r

            
