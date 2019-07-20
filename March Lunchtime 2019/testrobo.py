T=input()
for t in range(T):
    n,x= map(int,raw_input().split())
    s=raw_input()
    p=0
    mR,mL=0,0
    for i in s:
        p= (p+1) if i=='R' else (p-1)
        #print i,p
        mR = max(mR,p)
        mL = min(mL,p)
    print 1+mR-mL
