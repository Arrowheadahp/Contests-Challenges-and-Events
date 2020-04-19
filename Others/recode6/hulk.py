
T=input()
for t in range(T):
    l,r=map(long,raw_input().split())
    n=long((10**9)+7)
    print (((r-l+1)%n)*((r+l-1)%n))%n
