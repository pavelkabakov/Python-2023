# Задача №51. Общее обсуждение
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: values = [0, 2, 10, 6]  Вывод: same
# ------------ Решение ----------------
# def same_by(characteristic, objects):
#     for i in objects:
#         if (characteristic(objects[0])) != (characteristic(i)):
#             return False
#     return True

# # def same_by(func, collection):
# #     return len(list(filter(func, collection))) == 0

# values = [0, 2, 10, 6]
# # values = []
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')
# --------------------------------------

# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке

# Ввод: пара-ра-рам рам-пам-папам па-ра-па-дам 
# Вывод: Парам пам-пам
# -------------- Решение ---------------------
# input = "пара-ра-рам рам-пам-папам па-ра-па-дам"
# letters = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
# a = list(map(lambda x: len(list(filter(lambda y: y in letters, x))), input.split()))
# if max(a) == min(a):
#     print("Парам пам-пам")
# else:
#     print("Пам парам")

# input = "пара-ра-рам рам-пам-папам па-ра-па-дам"
# for i in phrases:
# 		countVowels.append(len([x for x in i if x.lower() in vowels]))
	
# 	if countVowels.count(countVowels[0]) == len(countVowels):
# 		print('Парам пам-пам')
# 	else:
# 		print('Пам парам')
# -----------------------------------------
# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.

# Ввод: print_operation_table(lambda x, y: x * y)

# Вывод:
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36
# ----------- Решение ---------------------

def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        print(*list(map(operation, [i] * num_columns, range(1, num_columns + 1))))

print_operation_table(lambda x, y: x * y)