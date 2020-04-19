def try1(n, m, M):
    for i in range(n):
        S = []
        m = M[i][0]
        for j in range(1,m):
            if S != [] and S[-1] == M[i][j]:
                S.pop()
            else:
                S.append(m)
                m = M[i][j]







for _ in range(input()):
    n, m = map(int, raw_input().split())
    M = []
    for _ in range(n):
        M.append(map(int, raw_input().split()))

    print try1(n, m, M)
