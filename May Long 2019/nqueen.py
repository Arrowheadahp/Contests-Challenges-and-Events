def check(q):
    global C
    if q in C:
        return False

    h=len(C)
    i=0
    for j in C:
        if i+j==h+q or i-j==h-q:
            return False
        i+=1
    return True


for _ in xrange(input()):
    n=input()

    C=[]
    s=-1
    while len(C)<n:
        for i in range(s+1,n):
            if check(i):
                C.append(i)
                s=-1
                break

        else:
            s=C.pop(-1)
        #print C
            

    
        
    for i in range(n):
        s=''
        for j in xrange(n):
            if j==C[i]:
                s+='Q'
            else:
                s+='\\'
        print s
