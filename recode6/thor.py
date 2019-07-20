T=input()
for t in range(T):
    a,b,c=map(int,raw_input().split())
    x,y,z=a**2,b**2,c**2
    if x+y==z or y+z==x or z+x==y:
        print 'YES'
    else:
        print 'NO'
