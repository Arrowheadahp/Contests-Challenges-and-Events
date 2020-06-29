from collections import defaultdict

def RE():
    return [int(i) for i in raw_input().split()]

def buti(A):
    t = A[0]
    L = []
    n = 1
    for a in A[1:]+[2]:
        if a == t:
            n+=1
        else:
            L.append(n)
            t = a
            n = 1
    
    if A[0] == A[-1]:
        L[0] += L.pop()

    if A[0] == 0:
        L.append(L.pop(0))
    return L

for _ in range(input()):
    n = input()
    A = RE()

    s = sum(A)
    if s <= 1:
        print -s
        continue

    C = 0
    L = buti(A)
    for i in range(len(L)):
        if i%2==0:
            if L[i] == 1:
                C+= min(L[i-1], L[i+1])+1
            else:
                C+= L[i]/2+L[i]%2
    print C

    

    

    
        
