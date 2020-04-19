size = 5


def check(n):
    return n == (int(n**0.5))**2


def check2(L, T):
    s = 0
    for i in L:
        s += int(i)**2
    return check(s+T)


def sumsq(L):
    s = 0
    for i in L:
        s += int(i)**2
    return s


def brute(n):
    s = '1'*n
    while True:
        if '0' in s or not check(sumsq(s)):
            s = str(int(s)+1)
        else:
            return s


def better(n):
    if n < size:
        return brute(n)
    else:
        T = n-size
        s = '1'*(size)
        while True:
            if '0' in s or not check2(s, T):
                s = str(int(s)+1)
            else:
                return '1'*T+s

def bla():
    m = 0
    for t in range(1, int(input())+1):
        #n = input()
        ans = int(better(t))
        m = max(m, ans-int('1'*t))
        #print t, ans, m
    print m

def main():
    for _ in range(input()):
        n = int(input())
        print better(n)
main()
