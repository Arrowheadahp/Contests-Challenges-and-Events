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

def main():
    for _ in range(input()):
        n = input()
        A = map(int, raw_input().split())

        print func2(n, A)
main()
