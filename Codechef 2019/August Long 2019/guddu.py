def func1(n, A):
    c = 0
    for i in range(n):
        for k in range(i+1, n):
            x = 0
            for a in A[i: k+1]:
                x = x^a
            y = 0
            for j in range(i, k):
                y = y^A[j]
                x = x^A[j]
                if x == y:
                    c+=1
    return c



from collections import Counter

def func2(n, A):
    M = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        x = 0
        for a in range(i,n):
            x = x^A[a]
            M[i][a] = x

    c = 0
    for i in range(1,n):
        R = Counter(M[i])
        C = Counter([M[j][i-1] for j in range(i)])
        #print R,'\t',C

        for i in R:
            if i in C:
                c+=R[i]*C[i]
    return c
def func3(n, A):
    M = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        x = 0
        for a in range(i,n):
            x = x^A[a]
            M[i][a] = x

    for I in M:
        for J in I:
            print J,'\t',
        print
    print

    c = 0
    for i in range(1,n):
        R = Counter(M[i])
        C = Counter([M[j][i-1] for j in range(i)])
        #print R,'\t',C
        #print (Counter(R) & Counter(C))

        for i in R:
            if i in C:
                c+=R[i]*C[i]
    return c










def func(L):
    c=0
    for i in range(1,len(L)):
        for j in range(i):
            c+=L[i]-L[j]-1
    return c


def fn2(L):
    n=len(L) -1
    c = -1*(n*n+n)/2
    for i in L[::-1]:
        c += n*i
        n -= 2
    return c

def func4(n,A):
    x = 0
    D = {0:[0]}
    for i,a in enumerate(A):
        x = x^a
        if x in D:
            D[x].append(i+1)
        else:
            D[x] = [i+1]

    #print 'D=\t',D
    c = 0
    for d in D:
        if len(D[d])>1:
            c+=fn2(D[d])
    return c









    
def main():
    for _ in range(input()):
        n = input()
        A = map(int, raw_input().split())

        print func3(n, A)


from random import randint
def debug(f1 = func2, f2 = func4):
    for _ in range(64):
        n = 20
        A = [randint(0,63) for _ in range(n)]

        if f1(n, A) != f2(n, A):
            print A
            print f1(n,A)
            print func3(n,A)
            print
            print
    print 'dbc'
debug()
