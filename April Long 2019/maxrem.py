_=input()
A= map(int, raw_input().split())
high,shigh=0,0
for i in A:
    if high<i:
        shigh=high
        high=i
print shigh
    
