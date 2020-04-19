from math import ceil


def chefmax(A): return sum(A[:int(ceil(len(A)*1.0/2))])


def ramsmax(A): return sum(A[len(A)/2:])


def turn(M, p):
    mr = 0
    for i, r in enumerate(M):
        t = [chefmax, ramsmax][p](r)
        if t > mr:
            mr = t
            mi = i
    M[mi].pop(p)


for _ in range(input()):
    n = input()
    if n == 1:
        A = map(int, raw_input().split())[1:]
        print chefmax(A)
        continue

    M = []
    for _ in range(n):
        A = map(int, raw_input().split())[1:]
        M.append(A)
    
    
