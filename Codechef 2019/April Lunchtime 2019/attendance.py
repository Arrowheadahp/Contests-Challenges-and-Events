for _ in range(input()):
    n=input()
    fset=set()
    dset=set()
    A=[]

    for _ in range(n):
        name=raw_input()
        A.append(name)

        f=name.split()[0]

        if f in fset:
            dset.add(f)
        else:
            fset.add(f)

    for i in A:
        first=i.split()[0]
        if first in dset:
            print i
        else:
            print first
