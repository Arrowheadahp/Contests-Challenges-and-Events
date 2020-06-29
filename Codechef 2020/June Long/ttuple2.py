def RE():
    return [int(i) for i in raw_input().split()]

def isint(n):
    return n == int(n)

def double():
    def m(a, b):
        if (X[a]-X[b])%(A[a]-A[b]) != 0:
            return None
        return (X[a]-X[b])/(A[a]-A[b])

    if len(set(A)) == 3:
        M = [m(0, 1), m(1, 2), m(2, 0)]
        if None not in M and len(set(M)) == 1:
            return True


def check3(sub, div):
    P = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]

    if double():
        return '3*3+'
    
    for p in P:
        i, j, k = p

        if A[i] and A[j] and (X[i] - sub[k])*1.0/A[i] == (X[j] - sub[k])*1.0/A[j]:
            # **
            # +++
            if isint((X[i] - sub[k])*1.0/A[i]):
                return '2*3+'

        if (A[i]+sub[k]) and (A[j]+sub[k]) and 1.0*X[i]/(A[i]+sub[k]) == 1.0*X[j]/(A[j]+sub[k]):
            if isint(1.0*X[i]/(A[i]+sub[k])):
                return '3+2*'
                     

        if None not in div and div[i]*div[k] == div[j]:
            # **
            #  **
            return '2*2*'

        if sub[i]+sub[k] == sub[j]:
            # ++
            #  ++
            return '2+2+'

        if div[k] != None:

            c = div[k]
            if c == 0:
                continue

            if X[i]*1.0/c -A[i] == X[j]*1.0/c -A[j]:
                if isint(X[i]*1.0/c):
                    return '2+3*'

            if X[j]*1.0/c -A[j] == sub[i]:
                return '2+2*'

            if A[j]*c + sub[i] == X[j]:
                return '2*2+'

    return '2moveNA'
                         
        
        




            
def divide():
    d = []
    for a, x in Z:
        if a == 0:
            if x==0:
                d.append(1)
            else:
                d.append(2*10**9+x)
        else:
            if x%a != 0:
                d.append(None)
            else:
                d.append(x/a)
    return d
    

def ttuple():
    
    sub = [x-a for a, x in Z]
    div = divide()
    
    S = set(sub)
    D = set(div)
    
    S.discard(0)
    D.discard(1)
    
    ls = len(S)
    ld = len(D)
    

    if None in D:
        if ls < 3:
            return ls
        res = check3(sub, div)
        
##        print res
        return len(res)/2

    if ls > 2 and ld > 2:
        res = check3(sub, div)
        
##        print res
        return len(res)/2

    return min(ls, ld)



for _ in range(input()):
    A = RE()
    X = RE()
    Z = zip(A, X)

##    print A
##    print X

    print ttuple()

##    print

##D = {i: 0 for i in range(4)} 
##R = range(-2, 3)
##T = [(a, b, c) for a in R for b in R for c in R]
##S = set([tuple(zip(A, X)) for A in T for X in T])
##for Z in S:
##    A, X = [], []
##    for z in Z:
##        A.append(z[0])
##        X.append(z[1])
##    
##    res = ttuple()
##    D[res] +=1
##
####    if res == 3:
####        print Z, res
##print D



'''
10
4 5 6
10 12 12
4 5 6
9 11 7
4 5 6
5 12 12
4 5 6
8 11 7
4 5 6
10 12 7
4 5 6
9 11 12
4 5 6
9 11 13
4 5 6
5 8 8
4 5 6
8 30 18
4 5 6
7 7 7
'''

