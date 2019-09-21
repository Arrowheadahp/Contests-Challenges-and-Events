def fact(k):
    f = 1
    while k:
        f*=k
        k-=1
    return f


for _ in range(input()):
    n, k = map(int, raw_input().split())
    A = map(int, raw_input().split())
    A.sort()

    x = A[k-1]
    s = A[:k].count(x)
    t = A.count(x)
    #print s, t
    print fact(t)/(fact(s)*fact(t-s))


'''
2
4 2
1 2 3 4
4 2
1 2 2 2
'''
