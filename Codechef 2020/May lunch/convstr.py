from collections import defaultdict

def func():
    Sa = set(A)
    Sb = set(B)

    Da = defaultdict(set)
    for i, a in enumerate(A):
        Da[a].add(i)

    Db = defaultdict(set)
    for i, b in enumerate(B):
        Db[b].add(i)

    M = []

    for z in sorted(list(Sb), reverse = True):
        if z not in Sa:
            return False
        if len(Db[z]-Da[z])==0:
            continue
        if min([A[i] for i in Db[z]])<z:
            return False
        M.append(Da[z] | Db[z])
        
    return M

    

for _ in range(input()):
    n = input()
    A = raw_input()
    B = raw_input()

    M = func()
    if M == False:
        print -1
        continue

    print len(M)
    for m in M:
        print len(m),
        for i in m:
            print i,
        print
    

    
        
