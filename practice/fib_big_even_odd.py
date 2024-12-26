def fib_eo(n):

    a = 0
    b = 1

    for _ in range(n - 1):
        c = (a + b) % 10
        a = b
        b = c

    return "even" if b % 2 == 0 else "odd"

print(fib_eo(841645))
