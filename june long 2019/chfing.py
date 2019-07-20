for _ in range(int(input())):
    n,k = map(int, input().split())

    t = (k-1)//(n-1)
    print (((t+1)*(k-1) - (t*(t+1)*(n-1))//2)%1000000007)
    #print (((((k-1)//(n-1)+1)*(k-1))//2)%1000000007)
