for _ in range(int(input())):
    n = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    C = [20*A[i] - 10*B[i] for i in range(n)]
    print (max(max(C), 0))
