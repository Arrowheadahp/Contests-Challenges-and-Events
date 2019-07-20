for _ in range(input()):
    n=input()
    A=map(int,raw_input().split())
    B=map(int,raw_input().split())

    s=sum(B)

    Q=[s]
    for i in range(n):
        s+=A[i]-B[i]
        Q.append(s)

    print max(Q)
    
    
