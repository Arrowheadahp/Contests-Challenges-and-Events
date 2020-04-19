def pascal(n):
    d = 1
    s = 1
    L = [[1, 1]]
    if n<=120000:
        while n-d > 500-len(L):
            s+=1
            L.append([s, 2])
            d+= s-1
        
        #print d, len(L)
        while n-d:
            if d == 1:
                s+=1
            L.append([s, 1])
            s+=1
            d+=1
        #print d, len(L)
    #return d
    return L
        
    


for q in range(input()):
    L = pascal(input())
    print 'Case #%d:'%(q+1)
    for i, j in L:
        #continue
        print i, j
