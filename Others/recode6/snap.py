
T=input()
for t in range(T):
    n=input()
    k=input()
    P=map(int,raw_input().split())
    d=k
    B=[0 for i in range(n)]
    s=0
    while j <2**n and d!=0:
    for i in range(n):
        s+=B[i]*P[i]
        if abs(d)>abs(s-k):
            d=s-k
        
