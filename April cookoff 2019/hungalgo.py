for _ in range(input()):
    n=input()
    flag=1
    l=[]
    for _ in range(n):
        a=map(int,raw_input().split())
        for i in range(1,n+1):
            if a[i-1]==0:
                l.append(i)
                flag=0
                
    if flag==1:
        print 'NO'

    else:
        l=set(l)
        for i in range(1,n+1):
            if i not in l:
                print 'NO'
                break
        else:
            print 'YES'
