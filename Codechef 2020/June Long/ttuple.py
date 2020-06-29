def checkzero(a,b,c,p,q,r):
    if a==p and b==q and c==r:
        return True
    return False
def checkone(a,b,c,p,q,r):
    diff=p-a
    if checkzero(a+diff,b,c,p,q,r) or checkzero(a+diff,b+diff,c,p,q,r) or checkzero(a+diff,b,c+diff,p,q,r) or checkzero(a+diff,b+diff,c+diff,p,q,r):
        return True
    if a!=0 and p%a==0:
        diff= p//a 
        if checkzero(a*diff,b,c,p,q,r) or checkzero(a*diff,b*diff,c,p,q,r) or checkzero(a*diff,b,c*diff,p,q,r) or checkzero(a*diff,b*diff,c*diff,p,q,r):
            return True
    return False           
def check1(a,b,c,p,q,r):
    if checkone(a,b,c,p,q,r) or checkone(b,c,a,q,r,p) or checkone(c,a,b,r,p,q):
        return True
    return False        
def checktwo(a,b,c,p,q,r):
    diff=p-a
    if check1(a+diff,b,c,p,q,r) or check1(a+diff,b+diff,c,p,q,r) or check1(a+diff,b,c+diff,p,q,r) or check1(a+diff,b+diff,c+diff,p,q,r):
        return True
    if a!=0:
        diff=p//a
        if check1(a*diff,b,c,p,q,r) or check1(a*diff,b*diff,c,p,q,r) or check1(a*diff,b,c*diff,p,q,r) or check1(a*diff,b*diff,c*diff,p,q,r):
            return True
    return False 
def check2(a,b,c,p,q,r):
    if checktwo(a,b,c,p,q,r) or checktwo(b,c,a,q,r,p) or checktwo(c,a,b,r,p,q):
        return True
    return False           
def newchecktwo(a,b,c,p,q,r):
    if (a-b)!=0:
        k=(p-q)/(a-b)
        x=(a*q-p*b)/(a-b)
        if k%1==0 and x%1==0:
            if checkzero(a*k+x,b*k+x,c*k,p,q,r) or checkzero(a*k+x,b*k+x,c*k+x,p,q,r) or checkzero(a*k+x,b*k+x,c+x,p,q,r):
                return True
    return False
def newcheck2(a,b,c,p,q,r):
    if newchecktwo(a,b,c,p,q,r) or newchecktwo(b,c,a,q,r,p) or newchecktwo(c,a,b,r,p,q):
        return True
    return False              

def works(a, b, c, p, q, r):
    if checkzero(a,b,c,p,q,r):
        print(0)
        continue
    if check1(a,b,c,p,q,r):
        print(1)
        continue
    if check2(a,b,c,p,q,r):
        #print(456)
        print(2)
        continue
    if newcheck2(a,b,c,p,q,r):
        #print(456)
        print(2)
        continue
    print(3)    
