def sim(s1, s2):
    c = 0
    while c <len(s1) and c<len(s2) and s1[c] == s2[c]:
        c+=1
    return c

def cleanse(L):
    t=0
    p = -1
    R = []
    for i in L:
        if p == i:
            t+=1
            if t == 3:
                t-=1
                continue
        else:
            t = 1
            p = i
        R.append(i)
    return R
        

def alien(n):
    L_input = [ raw_input() for _ in range(n) ]
    L = sorted([s[::-1] for s in L_input])
    score = [ sim(L[i], L[i+1]) for i in range(n-1) ]

    y = 0
    score = [0]+score+[0]
##    print score

    while score.count(0)!=len(score):
##        score = cleanse(score)
        m = score.index(max(score))
##        print score, m
        score[m-1:m+2] = [min(score[m-1], score[m+1])]
        y+=2
    
    return y



for q in range(input()):
    y = alien(input())
    print 'Case #%d: %d'%(q+1, y)
    
'''
4
2
TARPOL
PROL
3
TARPOR
PROL
TARPRO
6
CODEJAM
JAM
HAM
NALAM
HUM
NOLOM
4
PI
HI
WI
FI
'''
