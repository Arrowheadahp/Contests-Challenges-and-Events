import sys

def flush():
    sys.stdout.flush()

for _ in range(input()):
    n = input()
    mx = 10**n

    print 2*mx+input()
    flush()

    print mx - input()
    flush()

    print mx - input()
    flush()

    if input() == -1:
        sys.exit()

'''for _ in range(input()):
    n = input()
    m = 10**n
    
    a = input()
    print 2*m+a
    sys.stdout.flush()

    b = input()
    print m-b
    sys.stdout.flush()

    d = input()
    print m-d
    sys.stdout.flush()

    res = input()
    if res == -1:
        sys.exit()
'''
