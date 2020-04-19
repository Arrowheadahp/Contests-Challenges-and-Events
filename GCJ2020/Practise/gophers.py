import sys 
t, n, m = [int(i) for i in raw_input().split()]
W = [17, 16, 13, 11, 9, 7, 5]
for q in range(t):
    S = set(range(1, m+1))
    for w in W:
        s = (str(w)+' ')*18
        print s
        sys.stdout.flush()
        r = sum([int(i) for i in raw_input().split()])
        ws = set(range(r, m+1, w))
        S = S & ws
        #print ws
    print list(S)[0]
    sys.stdout.flush()
    if input() == -1:
        break
