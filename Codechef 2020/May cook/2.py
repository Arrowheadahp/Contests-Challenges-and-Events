for _ in range(input()):
    S = raw_input()

    a = S[0]
    index = [i for i, c in enumerate(S) if c == a]

    ai = index.pop(0)
    count = 0

    for zi in index:
        if S[ai:zi] == S[zi:2*zi]:
            T2 = S[2*zi:]
            tl = len(T2)/2

            if tl>0 and T2[:tl] == T2[tl:]:
                count+=1

    print count
        
