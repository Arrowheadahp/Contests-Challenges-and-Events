from sys import stdout

def query(i):
    print (i)
    stdout.flush()
    inp1 = int(input())

def complement():
    global B
    B = [1-i for i in B if i in [0,1]]

def check(s, d):
    global B
    if s != False and d == False:
        inp = query(s)
        _ = query(s)
        if inp != B[s]:
            complement()
    if s == False and d != False:
        inp = query(d)
        _ = query(d)
        if inp != B[d]:
            complement()
    if s != False and d != False:
        inp1, inp2 = query(s), query(d)
        if inp1 == B[s] and inp2 != B[d]:
            B.reverse()
        if inp1 == B[s] and inp2 == B[d]:
            B.reverse()
            complement()
        if inp1 == B[s] and inp2 == B[d]:
            complement()
        
        
    
    

def find(b):
    B = [ -1 for _ in range(b)]
    same = False
    diff = False
    t = 0
    q = 0
    
    while q<150 and t<=b/2:
        if q%10 == 0:
            check(same, diff)
            q+=2
        q+=2
        inp1, inp2 = query(t+1), query(b-t)
        if same == False and inp1 == inp2:
            same = t+1
        if diff == False and inp1 != inp2:
            diff = t+1
        B[t], B[b-t] = inp1, inp2
    s = ''
    for d in B:
        s+=str(d)
    return s
        
            
            
            


T, b = [int(i) for i in input().split()]
for x in range(1, T+1):
    s = find(b)
    print ('Case #%d: %s'%(x, s))
    stdout.flush()
    v  = input()
    if v == 'N':
        break
