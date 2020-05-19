def comp(m, k, n):
    if k>m*n or k<n:
        return
    if n == 1:
        return [[k]]
    M = []
    for i in range(1, m+1):
        L = comp(m, k-i, n-1)
        if L != None:
            #print L
            for r in L:
                M.append(r+[i])
    #print M
    return M


def backtrack(M, CS, RS, row, col):
    global SET, n
    for r in M:
        if set(r) != SET:
            break
    else:
        return True

    if row == col:
        return backtrack(M, CS, RS, row, col+1)

    P = list(SET - RS[row] - CS[col])
    for p in P:
        M[row][col] = p
        RS[row].add(p)
        CS[col].add(p)
        if backtrack(M, CS, RS, row+(col+1)/n, (col+1)%n):
            return True
        M[row][col] = 0
        RS[row].remove(p)
        CS[col].remove(p)
    return False
    
            
            

def diag(n, k):
    M = comp(n, k, n)
    #print M
    S = []
    for i in M:
        if sorted(i) not in S:
            S.append(sorted(i))
    return S
    

for x in range(1, input()+1):
    n, k = [int(i) for i in raw_input().split()]
    SET = set(range(1, n+1))

    print 'Case #%d:'%(x),

    D = diag(n, k)
    for d in D:
        M = [[0 for _ in range(n)] for _ in range(n)]
        CS = [set() for _ in range(n)]
        RS = [set() for _ in range(n)]
        for i in range(n):
            M[i][i] = d[i]
            CS[i].add(d[i])
            RS[i].add(d[i])

        if backtrack(M, CS, RS, 0, 0):
            break
    else:
        print 'IMPOSSIBLE'
        continue
    print 'POSSIBLE'
    for r in M:
        for c in r:
            print c,
        print

        

        





















    
