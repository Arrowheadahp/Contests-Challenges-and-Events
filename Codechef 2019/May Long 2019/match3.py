import sys
sys.setrecursionlimit(1000000)


def pred(a,b,t):
    r=a%b
    if r==0:
        return t

    if a>b*2:
        return t

    return pred(b,r,1-t)


for _ in xrange(input()):
    L=map(long,raw_input().split())

    win=pred(max(L),min(L),0)

    print ['Ari','Rich'][win]


'''
9
1 1
2 2
1 3
155 47
6 4
10 4
14 4
5 7
5 12
'''
