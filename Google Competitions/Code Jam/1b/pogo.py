xor = lambda a, b: ((a)^(b))%2

def one(pos):
    for i, p in enumerate(pos):
        if p%2:
            return i
    return -1
            

def func(pos):
    global s
    #print pos, s
    
    a, b = pos
    if pos == [0, 0]:
        return s


    if xor(a, b) == 0:
        s = 'IMPOSSIBLE'
        return s
    
        

    d = one(pos)
    t = xor(a/2, b/2)
    L = [['W', 'E'],
         ['S', 'N']]

    if 0 in pos:
        if 1 in pos:
            s+= L[d][1]
            return s
        if -1 in pos:
            s+= L[d][0]
            return s
    s+=L[d][t]

    if t == 0:
        pos[d]+=1
    
    
    
        
    pos = [i/2 for i in pos]
    func(pos)
    




    

for q in range(input()):
    pos = [int(i) for i in raw_input().split()]
    s = ''
    x = func(pos)

    print 'Case #%d:'%(q+1), s
