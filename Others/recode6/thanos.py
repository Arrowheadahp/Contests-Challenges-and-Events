
n,d,e=map(int,raw_input().split())
s=raw_input()
r=e-d
rs=''
for a in s:
    x=ord(a)+r
    y=(x-97)%26
    rs+=chr(y+97)
print rs
        
            
        
