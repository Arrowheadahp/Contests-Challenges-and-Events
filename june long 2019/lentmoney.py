def proc3(n,A,k,x):

    C=[(a^x)-a for a in A]
    C.sort(reverse=True)

    xsum=sum(A)

    #print A
    #print C
    flag=0

    
    for i in xrange(k,n+1,k):
        sl=C[i-k:i]
        s=sum(sl)
        if s>0:
            xsum+=s
            flag=1
        else:
            break
    else:
        i=n
    if flag==0:
        return xsum
    print xsum
    
    mx=0
    for j in xrange(k):
        if i-k-j>=0:
            sl= C[i-k-j:i-j]
            for t in xrange(j):
                sl[t]=sl[t]*(-1)

            mx=max(mx,sum(sl))
    return xsum+mx




def main():
    for _ in xrange(input()):
        n= input()
        A= map(int, raw_input().split())
        k=input()
        x=input()

        ans= proc3(n,A,k,x)
        print ans
        
main()
'''
7
5
1 2 3 4 5
2
4
7
10 15 20 13 2 1 44
4
14
10
10 15 20 13 2 1 44 0 99 14
4
14
6
20 10 13 44 15 14
4
14
8
10 10 13 44 15 14 14 44
4
14
9
20 20 20 20 20 20 20 20 20
4
14
4
20 20 20 20
4
14
'''
