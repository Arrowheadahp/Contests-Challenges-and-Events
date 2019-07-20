def proc5(n,A,k,x):
    C=[(a^x)-a for a in A]
    sA=sum(A)

    if n==k:
        return max(sum(C)+sA,sA)

    inv=0
    spos=0
    mn=10**9
    
    for c in C:
        if c>0:
            inv+=1
            spos+=c
        mn=min(mn,abs(c))

    if k%2==0 and inv%2==1:
        spos-=mn
        
    return spos+sA

def main():
    for _ in xrange(input()):
        n= input()
        A= map(int, raw_input().split())
        k=input()
        x=input()
        
        print proc5(n,A,k,x)
        
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
