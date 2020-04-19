for _ in xrange(input()):
    n = input()
    s=raw_input()

    v='aeiou'
    I=0

    for i in xrange(1,n):
        if s[i] in v:
            if s[i-1] not in v:
                I+=1

    print I
            
