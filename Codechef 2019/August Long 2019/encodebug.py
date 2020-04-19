def f(x):
    nl = []
    p = 'XXX'
    for i in x:
        if i == p:
            nl.append(0)
        else:
            p = i
            nl.append(i)
    integer=0
    for i,j in enumerate(nl[::-1]):
        integer += j*10**i
    #print integer
    return integer

def brute(L,R):
    s = 0

    e = long(R)
    x = long(L)
    while x <= e:
        y = map(int, list(str(x)))
        s+=f(y)
        x = x+1
    return str(s)









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





def divide(L, R):
    DL = [0, 45, 4905, 494550, 49495500, 949954972, 999546542, 995153507, 920350007, 85000028,
          2457, 242865, 24258150, 425531486, 550313306, 2980215, 14521500, 617150014, 365001169,
          118629, 11882745, 188472943, 849278674, 947711812, 969630542, 947553514, 600350602,
          485058394, 5825169, 582377985, 236408944, 627002739, 561358466, 746696222, 778121780,
          897178434, 567852500, 285346845, 535656709, 575394579, 636698001, 642204652, 944514689,
          691967563, 601749013, 224832812, 982600366,
          253229079, 254839375, 803253832, 518547689, 786419019, 958406121, 5659077, 216384176]
    
    ll = len(L)
    lr = len(R)

    s = 0
    mod = 10**9+7
    if lr-ll > 1:
        s = DL[lr-1] - DL[ll]

        s = (s + long(func2(L, '9'*ll)) +
             long(func2('1'+'0'*(lr-1), R)))%mod

    else:
        s = func2(L, R)

    return str(s)

def minus():
    pass



from random import randint
def debuff():
    for i in range(1000):
        L = str(randint(10, 10**3))
        R = str(randint(10**3+1, 10**4))

        b = func2(L, R)
        f = divide(L, R)

        print i

        if b!=f:
            print 
            print L, R
            print b, f
            print
    print 'done'









def modexp(a,b,c):
    # calculating a**b%c
    
    res = 1
    i=0
    while b>0:
        bit = b%2
        b = b/2
        res = (res * a**bit) % c
        a = (a*a)%c
        
    return res
    
def insight():
    L = [0, 45]
    #P = []
    for i in range(2, 10**2+1):
        #P.append(func2('0', str(10**i-1)))
        x = int((L[-1]*10+ 45*(modexp(10, 2*i-2, 10**9+7) -
                               modexp(10, 2*i-4, 10**9+7))))%(10**9+7)
        L.append(x)
        print x,',',
    #print L
    #print P

insight()
