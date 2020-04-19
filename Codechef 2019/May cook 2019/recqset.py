for _ in xrange(input()):
    n=input()
    A=map(int,raw_input().split())

    pd=None
    try:
        for i in range(4):
            d=A[i+1]-A[i]
            if pd==d:
                D=d
                I=i
                break
            pd=d
    except:
        I=0
        D=(A[3]-A[0])/3

    for a in xrange(-I,n-I):
        print a*D+A[I],
    print
