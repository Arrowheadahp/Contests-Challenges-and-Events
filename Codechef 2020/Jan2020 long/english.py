def ip(s):
    if len(s)<2:
        return s
    return s[0]+s[-1]+ ip(s[1:-1])

def ipi(s):
    if len(s)<2:
        return s
    return s[0]+ipi(s[2:])+s[1]

def b(k1, k2):
    b=0
    l1, l2 = list(k1), list(k2)
    while len(l1)>0 and len(l2)>0:
        if l1.pop() == l2.pop():
            b+=1
        else:
            break
    return b

def bn(s1,s2):
    l1 = list(ipi(s1))
    l2 = list(ipi(s2))
    #print l1, l2
    return (min(b(l1, l2), b(l1[::-1], l2[::-1])))**2
        
'''
for _ in range(input()):
    n = input()
    W = [raw_input() for _ in range(n)]

    I = sorted([ip(w) for w in W])
    res = 0
    for i in range(0, n-1, 2):
        res+= bn(I[i], I[i+1])

    print res
    '''

for _ in range(input()):
    n = input()
    W = [raw_input() for _ in range(n)]

    I = sorted([w[len(w)/2:] for w in W])

    res = 0
    for i in range(0, n-1, 2):
        res+= b(I[i], I[i+1])**2
    print res















    
