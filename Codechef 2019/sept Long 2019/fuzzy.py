from collections import Counter
def hcf(a, b):
    while b:
        a, b = b, a%b
    return a

n = input()
A = map(int, raw_input().split())

M = []
for i in range(n):
    h = A[i]
    L = []
    for j in range(i, n):
        h = hcf(h, A[j])
        L.append(h)
    M.append(L[::-1])

L=[]
for i in range(n):
    for j in range(i+1):
        L.append(M[j][i-j])

#for i in M:
    #print i
for _ in range(input()):
    k = input()
    c = 0
                 
    for i in L:
        if k%i == 0:
            c+=1
        else:
            break
    print c
