for _ in range(input()):
    n = input()
    s = raw_input()

    A = [-1 for _ in range(130)]
    m = 0

    for i, c in enumerate(s):
        o = ord(c)
        if A[o] == -1:
            A[o] = i
        else:
            m = max(m, n-i+A[o])
            A[o] = i
    
    print m