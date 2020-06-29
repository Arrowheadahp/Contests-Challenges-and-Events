def ceil(n):
    if n%2:
        return n/2+1
    return n/2

for _ in range(input()):
    n = input()
    b = bin(n)[3:]
    if b == '0'*len(b):
        print -1
        continue
    
