for _ in range(input()):
    n = input()
    S,x=map(str,raw_input().split())
    
    indices= [i for i,j in enumerate(S) if j==x ]  # for making the list of indices
    
    
    s,j=0,-1
    for i in indices:
        #print s
        s=s+(i-j)*(n-i)
        j=i

    print s
