# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 
# ----- Решение ----------
# def Pow_1(a=0, b=0, result=0):
#     if b > 0 and a > 0: # вычисление степени числа
#         if result == 0: result  = 1
#         result = result*a
#         b -= 1
#         return Pow_1(a, b, result)
#     elif b == 0 and result == 0: # отсекаем нулевую степень
#         result = 1
#         return result
#     elif b < 0 and a > 0: # вычисляем отрицательную степень числа
#         if result == 0: result  = 1
#         result = result*a
#         b += 1
#         if b < 0: return Pow_1(a, b, result)
#         return Pow_1(a, b, 1/result)
#     elif a == 0 and result == 0: # если нулевое число возвращаем 0
#         return result    
#     else:
#         return result

# a = 3 # number
# b = 5 # pow
# print(Pow_1(a, b))

# ------------------------
# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*

# 2 2
#     4 
# ----- Решение ----------
def sum(a=0, b=0, summa=0):
    if a != 0:
        summa += 1
        a -= 1
        return sum(a, b, summa)
    elif b != 0:
        summa += 1
        b -= 1
        return sum(a, b, summa)
    else:
        return summa
    
print(sum(2, 2))
# ------------------------
