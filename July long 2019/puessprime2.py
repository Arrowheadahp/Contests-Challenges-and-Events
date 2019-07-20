import sys
def primality(n):
    b = bin(n-1)[2:]
    b = b[::-1]
    for i in range(2,min(n, 3)):
        rem = 1
        p=-1
        for j in b:
            p+=1
            rem = (rem* i**(int(j)*2**p))%n
        if rem!=1:
            return False
    return True

def hcf(a,b):
    while b:
        a,b = b,a%b
    return a

for _ in xrange(input()):
    sys.stdin.flush()
    h = None

    for x in [31662,31669,64339,31702,31638]:
    
        print 1,x
        sys.stdout.flush()
        sys.stdin.flush()
        
        r = input()
        sys.stdin.flush()
        
        d = x**2-r
        if not h:
            h = d
        h = hcf(h, d)
        
            
        

    

    print 2,h
    sys.stdout.flush()
    sys.stdin.flush()
    verdict = raw_input()
    sys.stdin.flush()
    if verdict != 'Yes':
        break 
