for x in range(1, input()+1):
    n = input()
    M = sorted([ [int(i) for i in raw_input().split()] + [m]
                                  for m in range(n) ],
                                   key = lambda t: t[0])

    K = ['a' for _ in range(n)]
    onC, onJ = 0, 0
    for s, e, i in M:
        if s>=onC:
            K[i] = 'C'
            onC = e
        elif s>=onJ:
            K[i] = 'J'
            onJ = e
        else:
            K = list('IMPOSSIBLE')
            break

    ans = ''
    for i in K:
        ans+=i
    print 'Case #%d: %s'%(x, ans)
            


'''
3
5
1 6
6 9
3 6
6 10
9 10
5
1 6
6 9
3 6
6 10
8 10
4
1 3
1 5
4 8
6 8
'''
