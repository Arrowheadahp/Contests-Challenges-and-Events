from collections import Counter


def property(s):
    v = set('aeiou')
    counter = 1
    if s[0] in v:
        counter = -1
    for c in s[1:]:
        if c in v:
            if counter <0:
                continue
            else:
                counter-=1
        else:
            counter +=1
            if counter>0:
                return False
    return True


def dictmul(D):
    m = 1
    for i in D:
        if D[i]:
            m *= D[i]
    return float(m)


for _ in range(int(input())):
    xa, xb = Counter(), Counter()
    fa, fb = Counter(), Counter()
    a, b = 0, 0

    for _ in range(int(input())):
        i = str(input())
    
        if property(i):
            t = Counter(i)
            a += 1
            fa.update(t)
            xa.update(t.keys())
        else:
            t = Counter(i)
            b += 1
            fb.update(t)
            xb.update(t.keys())

    # print xa, fa
    # print xb, fb
    
    R = (dictmul(xa) * dictmul(fb)**b) / (dictmul(fa)**a * dictmul(xb))

    #R = num*1.0/den

    if R>10**7:
        print ('Infinity')
    else:
        print (R)
    
    
'''
2
4
aba
abc
bab
aac
3
aba
baab
abc

'''
    

    



    

    
