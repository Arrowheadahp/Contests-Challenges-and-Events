for _ in range(input()):
    c, x = map(int, raw_input().split())
    if x == 1:
        print c
        continue
    s = 0
    while c:
        s += c%x
        c = c/x
    print s
