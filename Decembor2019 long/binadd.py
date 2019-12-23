'''from sys import setrecursionlimit
setrecursionlimit(10**5)

def f(A, B):
    if B == 0:
        return 0
    
    return 1+ f(A^B, (A&B)<<1)


for _ in range(input()):
    A = int(raw_input(), 2)
    B = int(raw_input(), 2)

    c = 0
    while B>0:
         A, B = A^B, (A&B)<<1
         c+=1
    print f(A, B)
''
for _ in range(input()):
    A = raw_input()
    B = raw_input()

    m = max(len(A), len(B))

    A = A.zfill(m)[::-1]
    B = B.zfill(m)[::-1]

    if int(B, 2) == 0:
        print 0
        continue

    mx = 1
    c = -1
    for i in range(m):
        a = int (A[i])
        b = int (B[i])
        print a, b, c
        if a&b:
            c = 2       

        elif c!=-1:
            c+=1
            if not a|b:
                mx = max(mx, c)
                c = -1
            
    print max(mx, c)
    '''
'''
for _ in range(input()):
    A = int(raw_input(), 2)
    B = int(raw_input(), 2)

    V = bin(A&B)[2:][::-1] + '0'
    U = '0' + bin(A|B)[2:][::-1]+'0'

    print U, V

    if B == 0:
        print 0
        continue

    zero = 0
    mx = 0
    one = V.find('1')
    while one != -1:
        zero = U[one+1:].find('0')
        diff = zero-one
        mx = max(diff, mx)
        one = V[zero+1:].find('1')
    print mx+1
    '''





def find(S, si, x):
    t = S[si:].find(x)
    if t == -1:
        return t
    else:
        return t + si



for _ in range(input()):
    A = raw_input()
    B = raw_input()

    if int(B, 2) == 0:
        print 0
        continue

    C = bin(int(A,2) ^ int(B,2))[2:][::-1] + '0'*(10**1)
    B = bin(int(A,2) & int(B,2))[2:][::-1] + '0'

    #print C, B
    
    z = 0
    mx = 0
    o = B.find('1')
    while o != -1:
        z = find(C, o+1, '0')
        mx = max(mx, z-o)
        o = find(B, z, '1')
    print mx+1
