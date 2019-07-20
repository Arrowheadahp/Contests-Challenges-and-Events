# cook your code here
for _ in xrange(input()):
    n = raw_input()
    
    s=0
    for d in n:
        s+=int(d)
    
    a=10-(s%10)
    print (n+str(a)[-1])
    
