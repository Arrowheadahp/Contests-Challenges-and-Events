from sys import stdout

def query(i):
    print i
    stdout.flush()
    return input()


def complement():
    global B
    B = [1-i for i in B]

def check(s, d):
    global B
    if s != False and d == False:
        inp = query(s)
        _ = query(s)
        if inp != B[s-1]:
            complement()
    if s == False and d != False:
        inp = query(d)
        _ = query(d)
        if inp != B[d-1]:
            complement()
    if s != False and d != False:
        inp1, inp2 = query(s), query(d)
        if inp1 == B[s-1] and inp2 != B[d-1]:
            B.reverse()
        if inp1 != B[s-1] and inp2 == B[d-1]:
            B.reverse()
            complement()
        if inp1 != B[s-1] and inp2 != B[d-1]:
            complement()
    #print B
        
    
    

def find(b):
    global B
    B = [ -1 for _ in range(b)]
    same = False
    diff = False
    t = 0
    q = 0
    
    while t<=b/2:
        if q%10 == 0:
            check(same, diff)
            if q:
                q+=2
        q+=2
        inp1, inp2 = query(t+1), query(b-t)
        if same == False and inp1 == inp2:
            same = t+1
        if diff == False and inp1 != inp2:
            diff = t+1
        B[t], B[b-t-1] = inp1, inp2
        t +=1
        #print B
    s = ''
    for d in B:
        s+=str(d)
    return s
        
            
            
            


T, b = [int(i) for i in raw_input().split()]
for x in range(1, T+1):
    s = find(b)
    print s
    stdout.flush()
    v  = raw_input()
    if v == 'N':
        break
