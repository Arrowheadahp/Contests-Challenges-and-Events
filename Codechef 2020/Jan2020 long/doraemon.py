def check1(i, j):
    t=1
    while i-t>=0 and i+t <n and j-t>=0 and j+t<m:
        if M[i+t][j] == M[i-t][j] and M[i][j+t]==M[i][j-t]:
            t+=1
        else:
            break
    return t
        
def check2(i, j):
    t = 1
    while (j-t)>=0 and (i-t)>=0 and i+t<n and j+t<m and M[i][j-t]==M[i][j+t] and M[i-t][j]==M[i+t][j]:
        t+=1
    return t
            

for _ in range(input()):
    n, m = map(int, raw_input().split())
    M = []
    for i in range(n):        
        M.append(map(int, raw_input().split()))

    count = 0
    for a in range(n):
        for b in range(m):
            count+= check2(a, b)
            
    print count
