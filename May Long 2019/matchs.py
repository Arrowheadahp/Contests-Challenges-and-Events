def euler(a,b):
    w=0
    while b:
        w=1+w
        a,b=b,a%b
        #print a,b
    #print w
    return w

for _ in xrange(input()):
    n,m=map(long,raw_input().split())

    x=euler(n,m)
    y=euler(m,n)
    
    if min(x,y)%2==0 and max(m,n)<2*min(m,n):
        print 'Rich'

    else:
        print 'Ari'
    
'''
9
1 1
2 2
1 3
155 47
6 4
10 4
14 4
5 7
5 12
'''
