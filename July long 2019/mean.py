for _ in xrange(input()):
    n=input()
    A= map(int,raw_input().split())

    m= 1.0*sum(A)/n
    if int(m)!=m:
        print 'Impossible'

    else:
        for i in range(n):
            if A[i]==int(m):
                print i+1
                break
        else:
            print 'Impossible'
