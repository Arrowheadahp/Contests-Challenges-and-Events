for _ in range(input()):
    n=input()
    A=map(int,raw_input().split())

    P=[0 for _ in range(30)]

    for a in A:
        t=a
        i=0
        while t:
            P[i]+=t%2
            t>>=1
            i+=1

    res=0
    for i in range(30):
        res+=min(P[i],n-P[i])<<i

    print res
