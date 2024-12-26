import numpy as np

def fib(n):
    # Вычисляем n-ое число Фибоначчи по формуле Бине
    phi = (1 + np.sqrt(5)) / 2
    psi = (1 - np.sqrt(5)) / 2

    return int((phi**n - psi**n) / np.sqrt(5) + 0.5)

# Пример использования функции
print(fib(32)) 
