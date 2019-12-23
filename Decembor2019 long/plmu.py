def f(n):
    return (n*(n-1))/2

        
        
for _ in range(input()):
    n = input()
    A = map(int, raw_input().split())
    two = A.count(2)
    zero = A.count(0)

    print f(two) + f(zero)
