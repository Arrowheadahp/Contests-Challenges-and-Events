from collections import Counter
t, s = map(int, raw_input().split())
for _ in range(t):
    n = input()
    A = map(int, raw_input().split())
    B = map(int, raw_input().split())

    if s == 1:
        A.sort()
        B.sort()
        C = set(B)
        C.add(A[0])

        for a, b in zip(A, B):
            if a>=b or a not in C:
                print 'NO'
                break
        else:
            print 'YES'
                    
    elif s == 2:
        C = Counter(A+B)
        for i in C:
            if C[i]>n:
                print 'NO'
                break
        else:
            print 'YES'
    
