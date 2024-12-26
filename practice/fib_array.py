def fib(n):
    # Создаем массив для хранения чисел Фибоначчи
    fib_array = [0, 1]

    # Если n больше или равно длине массива, продолжаем вычисления
    if len(fib_array) <= n:
        for i in range(len(fib_array), n + 1):
            # Вычисляем следующее число Фибоначчи и добавляем его в массив
            next_number = fib_array[i - 1] + fib_array[i - 2]
            fib_array.append(next_number)

    return fib_array

# Пример использования функции
print(fib(8)) # Вывод: [0, 1, 1, 2, 3, 5, 8, 13]
