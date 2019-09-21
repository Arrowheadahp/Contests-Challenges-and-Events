for _ in range(int(input())):
    n, k = [(i) for i in input().split()]
    if (n/k)%k :
        print ('YES')

    else:
        print ('NO')
