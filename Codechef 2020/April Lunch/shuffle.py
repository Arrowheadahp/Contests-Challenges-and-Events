from collections import defaultdict
def RE():
    return [int(i) for i in raw_input().split()]
for _ in range(input()):
    n, k = RE()
    A = RE()
    D = defaultdict(list)
    for i, num in enumerate(A):
        D[num].append(i)
    A.sort()
    for i, num in enumerate(A):
        for x,j in enumerate(D[num]):
            if (i-j)%k==0:
                D[num][x] = k+1
                break
        else:
            print 'no'
            break
    else:
        print 'yes'
        
    
