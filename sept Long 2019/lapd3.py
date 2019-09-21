for _ in range(input()):
    A, B, C = map(int, raw_input().split())
    
    s = 0
    if A<2 or C<2:
        return 0
    for b in range(1, B+1):
        x = b**2
        u = 1+x/(C-1)
        i = A-u
        v = 1+x/(A-1)
        j = C-v
        if i<=0 or j<=0:
            continue
        t = i*j
        c=0
        for a in range(min(b,u),min(b,A-1)):
            c+=x/a-v+1
        for a in range(min(b,v),min(b,C-1)):
            c+=x/a-u+1
        if A-1>b and C-1>b and (u<=b and v<=b):
            c+=1-(b-u)*(b-v)
        s = (s+t-c)%(10**9+7)
    print s
