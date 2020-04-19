def safe(new, prev):
    if prev == None:
        return True
    a, b = new
    c, d = prev
    if a==c or b==d:
        return False
    if a-b==c-d or a+b==c+d:
        return False
    return True


def pylon(n, prev):
    global M, row, col, L
    
    if n>= row*col:
        return True
    for i in range(row):
        for j in range(col):
            if M[i][j] == 0 and safe((i, j),prev):
                M[i][j] = n+1
                L.append((i, j))

                if pylon(n+1, (i, j)):
                    return True

                M[i][j] = 0
                L.pop()
    return False
                
    



for q in range(input()):
    row, col = [int(i) for i in raw_input().split()]
    M = [[0 for _ in range(col)] for _ in range(row)]
    L = []
    v = pylon(0, None)
    
    print 'Case #%d:'%(q+1),
    if v == False:
        print 'IMPOSSIBLE'
        
    else:
        print 'POSSIBLE'
        for i, j in L:
            print i+1, j+1
##        for m in M:
##            print m
