for _ in range(input()):
    A, b, C = map(int, raw_input().split())
    c = 0
    for B in range(1, b+1):
        x = B*2
        if A>B and C>B:
            c+=(A-B)*(C-B)-1

        #print c
        for i in range(1, min(B+1, A)):
            t= C-(x/(i-1))-1
            c+=max(t, 0)
            
        #print c
        for i in range(1, min(B+1, C)):
            t= A-(x/(i-1))-1
            c+=max(t, 0)
            

    print c
    #print

    

