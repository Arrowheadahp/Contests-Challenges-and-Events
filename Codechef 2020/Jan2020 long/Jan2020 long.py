for _ in range(input()):
    s, w1, w2, w3 = map(int, raw_input().split())

    if s > w1+w2+w3:
        print 1
    elif s > w1+w2 or s> w2+w3:
        print 2
    else:
        print 3
