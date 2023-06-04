# def sumNumbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa

# print(sumNumbers(10))



# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i - 2))


# print(list_1) # [1, 1, 2, 3, 5, 8, 13, 21, 34]

# Задача: факториал числа найти. вводите число и находите рекурсией его факториал.
#  для 5 факториал 120
# ------- decision -----------------
# n=10
# def fact(n):
#     if n in [0]:
#         return 1
#     return fact(n-1) * n

# print(fact(n)) # fact(10) = 3628800


# Задача No31. Решение в группах
# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи
# Input: 7 Output: 21
# Задание необходимо решать через рекурсию
# ------- decision -----------------
# n=10
# def fib(n):
#     if n in [0, 1]:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# print(fib(n))
# -----------------------------------------


