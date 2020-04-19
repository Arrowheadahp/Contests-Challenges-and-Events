for _ in xrange(input()):
    d= input()
    a= raw_input()

    p=0
    for i in a:
        if i=='P':
            p+=1

    req=d*.75
    x=0
    #print p,req

    for i in xrange(2,d-2):
        if x+p>=req:
            print x
            break

        if a[i]=='A':
            #print a[i+1:i+3]
            if 'P' in a[i-2:i]:
                if 'P' in a[i+1:i+3]:
                    x+=1
        if x+p>=req:
            print x
            break

    else:
        print -1
