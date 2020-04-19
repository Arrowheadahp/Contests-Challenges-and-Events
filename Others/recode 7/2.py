def func(n):
    if n<=2:
        return 1

    return 1+func(n%(n/2+1))

n = input()

print func(n)
