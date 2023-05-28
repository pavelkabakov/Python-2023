# ------------ ЗАДАЧА --------------
# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1
# ------------ РЕШЕНИЕ --------------
# import random
# n = 9 # number of elements
# x = 3
# list_1 = []
# for i in range(n):
#     number = random.randrange(0, 10)
#     list_1.append(number)
#     # print(f"i:{i}, number:{number}, list[i]: {list_1[i]}")
# print(list_1)
# print(f'кол-во вхождений числа {x} в списке = {list_1.count(x)}')


# ------------ ЗАДАЧА --------------
# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X

# 5
# 1 2 3 4 5
# 6
# -> 5
# ------------ РЕШЕНИЕ --------------
# import random
# n = 10 # number of elements
# x = 7
# list_1 = [0, 1, 2, 3, 4, 5, 5, 5, 6, 6, 6, 9, 9]
# # list_1 = []
# # for i in range(n):
# #     number = random.randrange(0, 10)
# #     list_1.append(number)
# list_1.sort()
# print(list_1)
# if list_1.count(x):
#     print(f'число {x} входит в список') 
# elif x <= min(list_1):
#     print(f'ближайший элемент в списке к числу {x} это: {min(list_1)}')
# elif x >= max(list_1):
#     print(f'ближайший элемент в списке к числу {x} это: {max(list_1)}')
# elif x > min(list_1) and x < max(list_1):
#     for i in range(len(list_1)):
#         if list_1[i] > x and (x - list_1[i-1] <= list_1[i] - x):
#             print(f'ближайший элемент в списке к числу {x} это: {(list_1[i-1])}')
#             break
#         elif list_1[i] > x and (list_1[i] - x < x-list_1[i-1]):
#             print(f'ближайший элемент в списке к числу {x} это: {(list_1[i])}')
#             break

# ------------ ЗАДАЧА --------------
# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.

# Ввод:
# ноутбук
# Вывод:
# 12
# ------------ РЕШЕНИЕ --------------
dict_1 = {'а':1, 'в':1,'е':1,'и':1,'н':1,'о':1,'р':1,'с':1,'т':1,
          'д':2,'к':2,'л':2,'м':2,'п':2,'у':2,
          'б':3,'г':3,'ё':3,'ь':3,'я':3,
          'й':4,'ы':4,
          'ж':5, 'з':5, 'х':5, 'ц':5, 'ч':5,
          'ш':8, 'э':8, 'ю':8,
          'ф':1, 'щ':1, 'ъ':1,}
word = 'ноутбук'
text_list = list(word)
print(f'длинна слова {word} : {len(word)} букв')
summ = 0
for i in text_list:
    summ = summ + dict_1[i]
print(f'стоимость слова \'{word}\' : {summ} баллов' )
# ------------ РЕШЕНИЕ --------------
