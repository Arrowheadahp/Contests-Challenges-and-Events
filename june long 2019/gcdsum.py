import time
from random import randint
def hcf(x,y):
    a,b=x,y
    while a:
        a,b = b%a,a
    return b


def progd(L,H):
    l=len(L)
    mx=L[-1]+1
    for i in xrange(l):
        g=H[0]
        if i==0:
            g=H[1]
        
        for j in xrange(l):
            if j!=i:
                g=hcf(g,H[j])
        mx=max(mx,g+L[i])
    return mx

def prog(L):
    mx=0
    for i in range(len(L)):
        h=L[i-1]
        for j in range(len(L)):
            if j!=i:
                h=hcf(h,L[j])
        mx = max(mx,h+L[i])
    return mx


def brute(A):
    mx=0
    for i in xrange(2**(len(A))):
        bn=bin(i)[2:]
        while len(bn)<len(A):
            bn='0'+bn
        L=[0,0]
        a=-1
        for b in bn:
            x=L[int(b)]
            a+=1
            if x:
                L[int(b)]=hcf(x,A[a])
            else:
                L[int(b)]=A[a]
        if sum(L) > mx:
            mx=sum(L)
            mxl=list(L)
    #print mxl,'\t',
    return mx

def furred(A):
    L=list(A)
    b=L.pop(0)
    while b+L[0]<L[-1]+1:
        while b+L[0]<L[-1]+1:
            b=hcf(b,L.pop(0))

        H=[]
        for i in L:
            H.append(hcf(b,i))

        b=max([b]+H)
    return prog([b]+L)

def fur(A,F=furred):
    L=F(list(A))
    r=L[0]
    H=[]
    for i in xrange(len(L)):
        H.append(hcf(r,L[i]))

    return(progd(L,H))

def chek(n,m=1000000000):
    return sorted(list(set([randint(1,m) for _ in xrange(n)])))


def red(L):
    #L=list(A)
    b=L.pop(0)
    while b+L[0]<L[-1]+1:
        b=hcf(b,L.pop(0))
    #print len(L)+1
    return [b]+L







def red2(L):
    d=1
    b=L[0]
    while b+L[d]<L[-1]+1:
        b=hcf(b,L[d])
        d+=1
    return [b]+L[d:]






def pred2(A):
    return prog(red2(list(A)))

















        
def pred(L):
    return(prog(red(L)))
    
def func(L):
    return L[1]



def prog2(A):
    L=red(A)
    print len(A),len(L)
    b=L[0]
    H=[[i,L[i]-hcf(b,L[i])] for i in range(len(L))]
    H.sort(reverse=True,key=func)

    mx=0
    hi=0
    for t in H:
        i=t[0]
        h=L[i-1]
        for j in range(len(L)):
            if j!=i:
                h=hcf(h,L[j])
        if h+L[i]>mx:
            mx=h+L[i]
            mxhi=hi
        hi+=1
        if mxhi>6:
            break 
    return mx
        
    





def stime (F):
    sumtime=0
    for i in range(10):
        #print i
        L=chek(100000)
        st=time.time()
        yo=F(L)
        t=time.time()-st
        sumtime+=t
        print t
    return sumtime
        



def main():
    for _ in xrange(input()):
        n= input()
        A=map(int, raw_input().split())
        print pred (A)
        #print fur(A)

def debug(F,n):
    e=0
    for i in xrange(n):
        L=chek(1000,1000)

        lhs=F(L)
        #print 'd',
        rhs=pred(L)
        if lhs!=rhs:
            #print 4
            for j in L:
                print j,
            print '\t',
            print lhs,rhs
            e+=1
    print e,'errors found'
    return e


debug(pred2,1000)
#print stime(red2)
#print 'minus',stime(furred)-stime(pred)

'''
17
4
4 4 7 6
3
3 5 6
4
3 5 6 7
4
33 11 71 71
4
96 40 60 96
4
91 40 12 91
4
29 48 58 48
4
57 65 65 57
4
97 92 97 36
4
4 4 4 4
4
28 60 76 93
4
14 30 64 93
4
10 60 15 72
4
22 58 76 97
4
22 46 32 79
4
36 30 44 75
4
60 15 25 78
'''

