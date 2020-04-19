def li(i, l):
    L = map(int, list(str(i)))
    L = [0 for _ in range(l-len(L)+2)]+L
    return L
    
def f1(x,pl = None):
    if pl == None:
        nl = []
        p = 'XXX'
        for i in x:
            if i == p:
                nl.append(0)
            else:
                p = i
                nl.append(i)
        return nl

def nex(x, pl):
    n = 1
    for i in x[::-1]:
        if i == 9:
            n+=1
        else:
            break

    
    nl = list(pl)
    
    nl[-1*n]=x[-1*n]+1
    if n>1:
        nl[-1*n+1] = 0
    if x[-1*n-1] == nl[-1*n]:
        nl[-1*n] = 0
    return nl
    

def func2(S, E):
    l = len(E)
    P = li(long(S), l)
    
    F = f1(P)
    SUM = list(F)

    i = long(S)
    e = long(E)
    while i < e:
        F = nex(li(i, l), F)
        #print i+1, F
        SUM = [SUM[j]+F[j] for j in range(l+2)]
        i+=1
        #print SUM
    #print SUM

    carry = 0
    ans = ''
    for i in SUM[::-1]:
        k = i+carry
        ans = str(k%10) + ans
        carry = k/10
    ans = str(carry)+ans
    return str(long(ans)%(10**9+7))
    
def main():
    for _ in range(input()):
        Nl, L = raw_input().split()
        Nr, R = raw_input().split()
        
        print func2(L, R)
        

def debug():
    n = f1([0,0]+map(int, list(str(985))))
    print n
    for i in range(985, 1112):
        n= nex([0,0]+map(int, list(str(i))), n)
        if n!=f1([0]+map(int, list(str(i+1)))):
            print i+1,'\t',n,'\t',f1([0]+map(int, list(str(i+1))))

main()

