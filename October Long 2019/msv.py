def brute(n, A):
    S = [0 for i in range(n)]
    for i in range(n-1):
        for j in range(i+1,n):
            if A[i]%A[j]==0:
                S[j]+=1
    print max(S)


for _ in range(input()):
    n = input()
    A = map(int, raw_input().split())

    brute(n, A)
