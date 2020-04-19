
def proc4(n,A,k,x):
    C=[(a^x)-a for a in A]
    C.sort(reverse=True)

    #print A
    #print C

    xsum=sum(A)
    flag=0

    for i in xrange(k,n+1,k):
        s=sum(C[i-k:i])
        if s>0:
            xsum+=s
            flag=1
        else:
            if flag==0:
                return xsum
            break
    else:
        i=i+k

    e=i-k
    mx=0
    xsum-= sum(C[e-k:e])
    for j in xrange(k):
        if e+j>n:
            break
        #print C[e-k+j:e+j]
        mx=max(mx,sum(C[e-k+j:e+j]))
    return xsum+mx

    
def func(L):
    return L[0]

def lret(L,n):
    return [l[n] for l in L]    

def proc1(n,A,k,x):
    B= [a^x for a in A]
    
    C= [[B[i]-A[i],A[i],B[i]] for i in xrange(n)]
    C.sort(key=func, reverse=True)

    D=[]

    for i in xrange(k,n+1,k):
        c=C[i-k:i]
        
        if sum(lret(c,0))>0:
            D=D+ lret(c,2)

        else:
            j=i-k
            break
    
    else:
        j=i
    D=D+ lret(C[j:],1)

    #return sum(D)

    print sum(D)
    print A
    print B
    print C
    print D
    print
    
    return sum(D)


def proc2(n,A,k,x):

    C=[(a^x)-a for a in A]
    C.sort(reverse=True)

    xsum=sum(A)
    for i in xrange(k,n+1,k):
        sl=C[i-k:i]
        s=sum(sl)
        if s>0:
            xsum+=s
        else:
            break
    else:
        i=n
    return xsum


def proc3(n,A,k,x):

    C=[(a^x)-a for a in A]
    C.sort(reverse=True)

    xsum=sum(A)

    print A
    print C

    
    for i in xrange(k,n+1,k):
        sl=C[i-k:i]
        s=sum(sl)
        if s>0:
            xsum+=s
        else:
            break
    else:
        i=n
    if i<=k:
        return xsum
    
    mx=0
    for j in xrange(k):
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
