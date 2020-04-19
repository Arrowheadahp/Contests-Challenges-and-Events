'''class item:
    def __init__(self, value, adjsum, nextitem = None):
        self.value = value
        self.adjsum = adjsum


class cllist:
    def __init__(self):
        self.last = None

    def add(self,item):
        item.nextitem = self.last

        if not self.last:
            self.last.nextitem = item

        self.last = item


for _ in xrange(input()):
    n = input()
    A = map(int, raw_input().split())

    Clist = cllist()
    for i in xrange(n):
        Clist.add(item(A[i], A[i]+A[(i+1)%n]))

    for '''

for _ in xrange(input()):
    n = input()
    A = map(int, raw_input().split())

    minadj = 10**9
    while n>0:
        n-=1
        adjsum = A[n] + A[n-1]
        if minadj > adjsum:
            minadj = adjsum
            minindex = n

    




        
        
