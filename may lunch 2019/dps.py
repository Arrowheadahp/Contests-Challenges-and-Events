for _ in xrange(input()):
    s = raw_input()

    D={}
    for a in s:
        if a in D:
            D[a] = 1-D[a]

        else:
            D[a] = 1

    n=0
    for d in D:
        if D[d] == 1:
            n+=1

    #print D
    if n >3 or n==0:
        print '!DPS'
    else:
        print 'DPS'
