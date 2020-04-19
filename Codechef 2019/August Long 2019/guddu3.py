def func(L):
    c = 0
    for i in range(1,len(L)):
        for j in range(i):
            c+=L[i]-L[j]-1
    return c

def fn2(L):
    n=len(L) -1
    c = -1*(n*n+n)/2
    for i in L[::-1]:
        c += n*i
        n -= 2
    return c

for _ in range(input()):
    n = input()
    A = map(int, raw_input().split())

    x = 0
    D = {0:[0]}
    for i,a in enumerate(A):
        x = x^a
        if x in D:
            D[x].append(i+1)
        else:
            D[x] = [i+1]

    #print D
    c = 0
    for d in D:
        if len(D[d])>1:
            c+=fn2(D[d])
    print c       

