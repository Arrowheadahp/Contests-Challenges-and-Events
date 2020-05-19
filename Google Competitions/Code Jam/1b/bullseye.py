import sys
#sys.stdout.flush()

def throw():
    global A
    gary = 'MISS'
    t = 10**9+1
    while gary == 'MISS':
        t-=1
        print 0, t
        sys.stdout.flush()
        gary = raw_input()

    gary = 'MISS'
    r = 10**9+1
    while gary == 'MISS':
        r-=1
        print  r, 0
        sys.stdout.flush()
        gary = raw_input()

    top = range(t-A-5, t-A+5)
    rig = range(r-A-5, r-A+5)

    for i in rig:
        for j in top:
            print i, j
            sys.stdout.flush()
            gary = raw_input()
            if gary == 'CENTER':
                return True
    return False
    
        

















T, A, B = [int(i) for i in raw_input().split()]

for q in range(T):
    x = throw()
    if x == False:
        break

