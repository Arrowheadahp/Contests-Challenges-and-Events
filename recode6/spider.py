
Q=input()
for q in range(Q):
    n=input()
    A=map(int,raw_input().split())
    A.sort()
    for i in range(1,n-1,2):
        A[i],A[i+1]=A[i+1],A[i]
    for a in A:
        print a,
    print
