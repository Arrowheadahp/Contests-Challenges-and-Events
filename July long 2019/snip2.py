def primality(n):
    b = bin(n-1)[2:]
    for i in range(1,min(n, 5)):
        rem = 1
        p=-1
        for j in b[::-1]:
            p+=1
            rem = (rem* i**(int(j)*2**p))%n
        if rem!=1:
            return False
    else:
        return True



def primelist(n):
    L=range(2,n)
    lim = n**0.5
    for i in range(len(L)):
        if L[i] and L[i]<lim:
            for j in range(i+1,len(L)):
                if L[j]:
                    if L[j]%L[i]==0:
                        L[j]=None
    return [p for p in L if p]

P = primelist(10**5)
#print (P)
print 'prime list created'

def dictcreate(d):
    D={}
    global P
    for p in P:
        r = d**2%p
        if r not in D:
            D[r] = []
        D[r].append(p)
    return D

def overlap(d):
    D = dictcreate(d)
    c=0
    for i in D:
        if len(D[i])>1:
            c+=1
    return c

def mindiv(a,b=10**5):
    m1=1000
    for i in range(a,b):
        c= overlap(i)
        if c<m1:
            print i,'\t',c
            m1,m2 = c,m1
        elif c<m2:
            print i,'\t',c
            m2=c
        if i%5000==0:
            print i,'\n'
    return (m1,m2)


mindiv(31625)
# 64339, 31662


def printdict(d):
    D = dictcreate(d)
    print d
    #return max([len(D[i]) for i in D])
    for i in D:
        if len(D[i])>2:
            print i,'\t',len(D[i]),'\t',D[i]

#printdict(31709)
#printdict(31662)

def compare(a,b):
    X=dictcreate(a)
    Y=dictcreate(b)

    for i in X:
        if len(X[i])>1 and i in Y:
            for j in X[i]:
                if j in Y[i]:
                    print i,'\t',X[i],'\t',Y[i]

#compare(64339, 31662)






        
