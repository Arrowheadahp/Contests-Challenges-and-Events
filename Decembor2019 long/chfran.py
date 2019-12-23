for _ in range(input()):
    n = input()
    S, E = [], []
    for _ in range(n):
        s, e = map(int, raw_input().split())
        S.append(s)
        E.append(e)
    
    S.sort()
    E.sort()
    C =[]

    #print S, E

    i = 0
    c = 0
    for e in E:
        if e < S[-1]:
            while i<n and S[i] <= e:
                c+=1
                i+=1
            c-=1
            C.append(c)
    #print C
    if C ==[]:
        print -1
    else:
        print min(C)
    
    '''
3
3
1 4
2 6
5 7
2
1 4
4 6
2
3 7
8 9
'''
