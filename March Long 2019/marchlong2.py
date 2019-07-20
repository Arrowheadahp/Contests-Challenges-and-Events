t=int(raw_input().lstrip())
for i in range(t):
    n,d= map(str,raw_input().split())
    r=''
    x=d
    for j in n[::-1]:
        if j>min(x,d):
            r=r+d
        else:
            r=j+r
        x=r[0]
    print int(r)
