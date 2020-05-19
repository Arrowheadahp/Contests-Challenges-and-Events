def func(R, S):
    global x
    if 1 in [R, S]:
        return True
    for i in range(1, S):
        x.append([R*(S-i), R-1])
    func(R-1, S)
    
    
    






    

for q in range(input()):
    x = []
    R, S = [int(i) for i in raw_input().split()]
    func(R, S)
##    L = [(i, j) for j in range(S) for i in range(R)]
##    print L

    print 'Case #%d:'%(q+1), len(x)
    for i, j in x:
        print i, j
##        A = L[:i]
##        B = L[i:i+j]
##        C = L[i+j:]
##        L = B+A+C
##        print L
##    print 
