x = 0
y = 1
t = 0
D = {}
for i in range(10**7):
    if i+1 == 2**t:
        D[t] = x
        t += 1
    x, y = y, (x+y)%10

print D
