def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# Пример использования функции
for i in range(6):
    print("fib(", i, ") =", fib(i))

import timeit

# Замер времени для fib(0)
setup_code = "from __main__ import fib"
stmt = "fib(0)"
time_fib0 = timeit.timeit(stmt=stmt, setup=setup_code, number=1000)
print("Время выполнения fib(0):", time_fib0, "мс")

# Замер времени для fib(5)
setup_code = "from __main__ import fib"
stmt = "fib(5)"
time_fib5 = timeit.timeit(stmt=stmt, setup=setup_code, number=1000)
print("Время выполнения fib(5):", time_fib5, "мс")


