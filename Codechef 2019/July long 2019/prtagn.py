'''
def check(n):
    b=bin(n)[2:]
    return b.count('1')%2


for _ in xrange(input()):
    q=input()

    S=set()
    R=[0, 0]
    for _ in xrange(q):
        x=input()
        if not x in S:
            R[check(x)]+=1
            for i in list(S):
                n= i^x
                R[check(n)]+=1
                S.add(n)
            S.add(x)
            print R[0], R[1]
'''
def count(n):
    global R,S
    R[bin(n)[2:].count('1')%2]+=1
    S.add(n)

for _ in xrange(input()):
    S=set()
    R=[0, 0]
    for _ in xrange(input()):
        x= input()
        if not x in S:
            for i in list(S):
                count(i^x)
            count(x)
        print R[0], R[1]
