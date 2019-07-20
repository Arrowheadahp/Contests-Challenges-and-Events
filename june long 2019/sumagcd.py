def hcf(a,b):
    while a:
        a,b = b%a,a
    return b

def prog(L):
    mx=0
    for i in range(len(L)):
        h=L[i-1]
        for j in range(len(L)):
            if j!=i:
                h=hcf(h,L[j])
        mx = max(mx,h+L[i])
    return mx
    
def red2(L):
    d=1
    b=L[0]
    while b+L[d]<L[-1]+1:
        b=hcf(b,L[d])
        d+=1
    return [b]+L[d:]




for _ in xrange(input()):
    n= input()
    A=map(int, raw_input().split())
    A=sorted(list(set(A)))
    if len(A) ==1:
        print A[0]*2

    else:
        print prog(red2(A))
