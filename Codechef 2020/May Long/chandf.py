for _ in range(input()):
    x, y, l, r = [int(i) for i in raw_input().split()]

    z = x|y
    bz = bin(z)[2:]
    while int(bz, 2)>r:
        bz = bz[1:]

    z = int(bz, 2)
    more = l-z
    if more<=0:
        print z
        continue

    print z
