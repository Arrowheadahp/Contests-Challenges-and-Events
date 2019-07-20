for _ in xrange(input()):
    num = input()
    S=raw_input()
    U=raw_input()

    score=0
    n=0
    for i in xrange(num):
        if n==1:
            n=0
            continue

        if S[i]==U[i]:
            score+=1
        elif U[i]=='N':
            continue
        else:
            n=1
    print score
            
            
