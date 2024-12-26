def fib(n):
    if n <= 1:
        return n
    else:
        a = 0
        b = 1
        for _ in range(n - 1):
            c = a + b
            a = b
            b = c
        return b

# Пример использования функции
print(fib(3)) # Вывод: 2
print(fib(7)) # Вывод: 13

from timeit import timeit

# Замер времени выполнения для разных значений n
times = {
    5: timeit("fib(5)", globals=globals(), number=1000),
    10: timeit("fib(10)", globals=globals(), number=1000),
    20: timeit("fib(20)", globals=globals(), number=1000),
    30: timeit("fib(30)", globals=globals(), number=1000),
    32: timeit("fib(32)", globals=globals(), number=1000)
}

# Вывод результатов замеров
for n, time in times.items():
    print("Время выполнения fib({n}) = {time:.3f} мс".format(n=n, time=time))
