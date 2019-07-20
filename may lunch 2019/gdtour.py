def hcf(a,b):
    while a:
        a,b=b%a,a
    return a

for _ in xrange(input()):
    n,m,k=map(int,raw_input().split())

    if hcf(m,k)==1 and hcf(n,k)==1:
        print m*n
    else:
        print -1
