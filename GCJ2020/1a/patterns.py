def patterns(n):
    P = [ raw_input() for _ in range(n) ]
    S = '*'
    for p in P:
        #print S, p
        pil = -p[::-1].find('*')
        sil = -S[::-1].find('*')
        mnl = min(pil, sil)
        mxl = max(pil, sil)
        if S[mxl:] != p[mxl:] and mxl<0:
            #print S[mxl:], p[mxl:]
            return '*'
        
        pis = p.find('*')
        sis = S.find('*')
        mns = min(pis, sis)
        mxs = max(pis, sis)
        if S[:mns] != p[:mns]:
            return '*'

        T = ''                       
        if pis>sis:
            T = p[:pis+1]
        else:
            T = S[:sis+1]
        T = T + S[sis:len(S)+sil] + p[pis:pil+len(p)]
        if pil<sil:
            if pil:
                T+= p[pil-1:]
        else:
            if sil:
                T+= S[sil-1:]
        S = T
    #return S
        
        
            


        
    y = ''
    for c in S:
        if c!='*':
            y+=c
    return y
                
                    

'''
6
5
*CONUTS
*COCONUTS
*OCONUTS
*CONUTS
*S
2
*XZ
*XYZ
5
p*
pr*
pra*
pras*
prasu*
3
p*
po*
o*
3
b*p*l
b*i*l
b*c*l
2
b*c*o
b*p*p
'''










for q in range(input()):
    y = patterns(input())
    print 'Case #%d: %s'%(q+1, y)
    
