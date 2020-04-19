for _ in xrange(input()):
    n,m=map(int,raw_input().split())
    menu={}

    for _ in xrange(n):
        d,v=map(int,raw_input().split())
        if d in menu:
            menu[d]=max(menu[d],v)
        else:
            menu[d]=v

    m1=0
    m2=0
    for i in menu.values():
        if i>m1:
            m1,m2=i,m1
        elif i>m2:
            m2=i

    print m1+m2
