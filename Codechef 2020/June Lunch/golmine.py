def RE():
    return [int(i) for i in raw_input().split()]

def func():
    R = range(n)
    G = [M[i][0] for i in R]
    A = [M[i][1] for i in R]
    B = [M[i][2] for i in R]

    F = [G[i]*1.0/A[i] for i in R]
    U = [G[i]*1.0/B[i] for i in R]

    F = sorted(enumerate(F), key = lambda t: t[1], reverse = True)
    U = sorted(enumerate(U), key = lambda t: t[1], reverse = True)

    fsum = 0
    usum = 0

    fex = 0
    uex = 0

    for f, u in zip(F, U):
        
        fi, fs = f
        ui, us = u

        if fi == ui:
            pass

        else:
            

      
        

for _ in range(input()):
    n = input()
    M = [RE() for _ in range(n)]
    
    
    func()

    
