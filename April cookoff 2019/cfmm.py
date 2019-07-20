for _ in range(input()):
    n=input()
    D={'c':0,'o':0,'d':0,'e':0,'h':0,'f':0}
    for _ in range(n):
        s=raw_input()
        for a in s:
            if a in D:
                D[a]+=1

    for j in 'ce':
            D[j]/=2

    print min([D[i] for i in 'codehf'])
