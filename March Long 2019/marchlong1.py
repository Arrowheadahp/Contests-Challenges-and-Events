t=input()
for i in range(t):
    n=input()
    A=map(int,(raw_input().split()))
    c,d,e=0,0,0
    for j in A:
        if j>0:
            c+=1
        elif j<0:
            d+=1
        else:
            e+=1
    print max(c,d)+e,
    if e>0:
        print 1
