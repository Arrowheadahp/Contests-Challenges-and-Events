for _ in range(input()):
    n, k = map(long, raw_input().split())

    if (n/k)%k:
        print 'YES'

    else:
        print 'NO'
