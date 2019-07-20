def check(r,c):
    global C
    global R

    '''print R
    print C'''
    #print r,c,
    
    for i in R[r]:
        if i!=c:
            for j in C[c]:
                if i in R[j]:
                    #print 'f'
                    return False
    #print 't'
    return True

for _ in xrange(input()):
    n=input()

    R=[[]]
    C=[[] for _ in xrange(n)]
    s=-1
    numR=0
    r=0
    
    while numR<8*n:
        flag=0
        #print numR
        for c in xrange(s+1,n):
            if check(r,c):
                R[-1].append(c)
                C[c].append(r)
                numR+=1
                flag+=1
                
        if flag<5:
            while len(R[r]
            s=R[-1].pop(-1)
            C[s].pop(-1)
            numR-=1
            continue

        r+=1
        R.append([])
        s=-1

    for i in xrange(n):
        s=''
        for j in xrange(n):
            if j in R[i]:
                s+='O'
            else:
                s+='.'
        print s
        
        
        
                
                
