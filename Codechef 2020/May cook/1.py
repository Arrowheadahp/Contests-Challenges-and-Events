from collections import Counter
for _ in range(input()):
    n = input()
    A = [int(i) for i in raw_input().split()]

    S = set()
    C = Counter(A)
    for a in C:
        if C[a] in S:
            print 'NO'
            break
        else:
            S.add(C[a])

    else:
        prev = -1
        S = set()
        for a in A:
            if a == prev:
                continue
            elif a in S:
                print 'NO'
                break
            else:
                S.add(a)
                prev = a
        else:
            print 'YES'

    
