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

def main():
    for _ in range(input()):
        Nl, L = raw_input().split()
        Nr, R = raw_input().split()
        

        print brute(L, R)
def insight():
    for i in range(985, 1112):
        print f(map(int, list(str(i))))

main()
