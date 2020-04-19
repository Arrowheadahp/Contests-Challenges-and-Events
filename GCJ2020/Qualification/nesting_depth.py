for x in range(1, int(input())+1):
    s = input()
    p = 0
    ans = ''
    for c in s:
        d = int(c)
        if d>p:
            ans+= (d-p)*'('
        else:
            ans+= (p-d)*')'
        ans+=c
        p = d
    ans+=p*')'

    print (f'Case #{x}: {ans}')
    
