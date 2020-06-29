for _ in range(input()):
    TS = input()
    T = bin(TS)
    loc = T[::-1].index('1')
    leftover = T[2:len(T)-loc-1]

##    print T, loc, leftover

    if leftover == '':
        print 0
        continue

    print int(leftover, 2)
    
'''
2
1
11
'''
