from collections import *
from math import *
inf = float('inf')

def RE():
    return [int(i) for i in raw_input().split()]

def func(q, D):
    D = [inf] + D + [inf]
    for _ in range(q):
        s, k = RE()
        li, ri = s-1, s
        room = s
        count = 1
        

        while count<k:
            l = D[li]
            r = D[ri]

            if l<r:
                room = li
                li-=1
            else:
                room = ri+1
                ri+=1
            
            count+=1
##            print l, r, room, count
                

        print room,
    return 0

##T = [1, 7, 5, 9, 1, 6, 1, 4, 2, 8, 11, 16, 13]
##func(10, T)



for query in range(input()):
    n, q = RE()
    D = RE()
    
    print 'Case #%d:'%(query+1),
    func(q, D)
    print
