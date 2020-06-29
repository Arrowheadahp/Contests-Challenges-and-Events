def RE():
    return [int(i) for i in raw_input().split()]

from collections import Counter

for _ in range(input()):
    r, c = RE()
    C = Counter()

    for _ in range(r):
        C.update(RE())

    odd = [i for i in C if C[i]%2]
    if (c%2 == 0 and len(odd)) or len(odd)>r:
        print -1
        continue
    

    L = []
    for i in C:
        L += [i for _ in range(C[i]/2)]
        
        
    M = []
    for i in range(r):
        K = []
        for j in range(c/2):
            K.append(L.pop())
        M.append(K)
        

    L = L + L + odd
##    print L
    if c%2:
        for row in range(r):
            M[row] = M[row] + [L.pop()] + M[row][::-1]
    else:
        for row in range(r):
            M[row] = M[row] + M[row][::-1]

    for row in M:
        for j in row:
            print j,
        print

    
        

    

    

    
