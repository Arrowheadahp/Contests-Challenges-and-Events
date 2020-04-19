def brute(A, B, C):
    s = 0
    for b in range(1, B+1):
        x = b**2
        for a in range(1, A):
            s+= max(0, C - (x/a)-1)
            #print c,
        #print s,
    return s%(10**9+7)

def func2(A, B, C):
    s = 0
    for b in range(1, B+1):
        x = b**2

        if A>b and C>b:
            s+=((A-b)*(C-b)-1)%(10**9+7)
        for a in range(1, min(A, b)):
            s+= max(0, C - (x/a)-1)
        for a in range(1, min(C, b)):
            s+= max(0, A - (x/a)-1)
        #print s,
    return s%(10**9+7)

def func3(A, B, C):
    s = 0
    for b in range(1, B+1):
        x = b**2

        if (A-1)*(C-1)<=x:
            continue

        if A>b and C>b:
            s+=((A-b)*(C-b)-1)%(10**9+7)
        for a in range(min(A, b)-1, 0, -1):
            t= max(0, C - (x/a)-1)
            if not t:
                break
            s+=t
        for a in range(min(C, b)-1, 0, -1):
            t= max(0, A - (x/a)-1)
            if not t:
                break
            s+=t
        #print s,
    return s%(10**9+7)

def func4(A, B, C):
    s = 0
    if A<2 or C<2:
        return 0
    for b in range(1, B+1):
        x = b**2
        u = 1+x/(C-1)
        i = A-u
        v = 1+x/(A-1)
        j = C-v
        if i<=0 or j<=0:
            continue
        t = i*j
        c=0
        for a in range(min(b,u),min(b,A-1)):
            c+=x/a-v+1
        for a in range(min(b,v),min(b,C-1)):
            c+=x/a-u+1
        if A-1>b and C-1>b and (u<=b and v<=b):
            c+=1-(b-u)*(b-v)
        s = (s+t-c)%(10**9+7)
    return s


def func5(A, B, C):
    s = func4(A, 1, C)
    t = s
    for b in range(2, B+1):
        t = t- min(2*b-1, C-b) - min(2*b-1, A-b)
        if A-1>b and C-1>b and (1+x/(C-1)<=b and 1+x/(A-1)<=b):
            t-=1
        s+=t
    return s
    


def main():
    for _ in range(input()):
        A, B, C = map(int, raw_input().split())
        
        #print brute(A, B, C),'\t'
        print func4(A, B, C)

def debug():
    t=range(1, 4)
    for i in t:
        for j in t:
            for k in t:
                if brute(i, j, k)!=func5(i, j, k):
                    print i, j, k, brute(i,j,k), func5(i,j,k)
    print 'd'

def x():
    a = func3(200, 1,210)
    for i in range(12):
        t = func3(200, i+1, 210)
        print i+1, t, a*(i+1)-t

debug()

























'''
4
2 5 3
3 2 4
11 4 10
11 4 8
'''
