def check(r,c):
    global C
    global R
    
    for i in R[r]:
        if i!=c:
            for j in C[c]:
                if i in R[j]:
                    return False 
    return True


def disp(R):
    for i in xrange(n):
        s=''
        for j in xrange(n):
            if j in R[i]:
                s+='O'
            else:
                s+='.'
        print s
        

for _ in xrange(input()):
    n=input()

    R=[[] for _ in xrange(n)]
    C=[[] for _ in xrange(n)]

    numR=0
    ri=0
    ci=-1

    while True:
        '''disp(R)
        print ri,ci
        print'''
        for r in xrange(ri,n):
            for c in xrange(ci+1,n):
                if check(r,c):
                    R[r].append(c)
                    C[c].append(r)
                    numR+=1
            ci=-1
            
        if numR>=n*8:
            disp(R)
            break

        while len(R[r])==0:
            r-=1
            
        ci=R[r].pop(-1)
        ri=C[ci].pop(-1)
        numR-=1
        




    

    
        
        
                
                
