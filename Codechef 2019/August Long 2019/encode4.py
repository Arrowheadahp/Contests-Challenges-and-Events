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
    for i in range(2, 10**5+1):
        #P.append(func2('0', str(10**i-1)))
        x = int((L[-1]*10+ 45*(modexp(10, 2*i-2, 10**9+7) -
                               modexp(10, 2*i-4, 10**9+7))))%(10**9+7)
        L.append(x)
    return L
    

def func3(X):
    global Y

    s=0
    X = X[::-1]
    for i in range(len(X)):
        c = int(X[i])
        if i == 0:
            s+= (c*(c+1))/2
        else:
            p = int(X[i+1])
            s+= (c-1)*(Y[i]) + (c*(c-1))/2*(10**(2*i) - 10**(2*i-2)) + (p+1)*Y[i] + (p+1)*6*10**i
            if p<c:
                s =s- c*10**(2*i-2)

            elif p==c:
                s = s- c*10**(i-1)*int(X[:i]




Y = insight()
def minus(L, R):
    
    return(func3(R) - func3(str(long(L)-1)))%(10**9+7)

def main():
    for _ in range(input()):
        Nl, L = raw_input().split()
        Nr, R = raw_input().split()
        
        print minus(L, R)
