# ---------псевдоним для функции --------------------------------
# def f(x):
#     return x ** 2
# g = f
# print(f(4)) # 16
# print(g(4)) # 16
# ---------псевдоним для функции --------------------------------
# def calc1(x):
#     return x + 10
# print(calc1(10)) # 20

# def calc2(x):
#     return x * 10
# def math(op, x):
#     print(op(x))
# math(calc2, 10) # 100
# ---------псевдоним для функции --------------------------------
# def sum(x, y):
#     return x + y
# def mylt(x, y):
#     return x * y
# def calc(op, a, b):
#     print(op(a, b))
# calc(mylt, 4, 5) # 20
# ---------то же самое через lambda --------------------------------
# def calc(op, a, b):
#     print(op(a, b))
# calc((lambda x, y: x + y), 4, 5) # 9
# calc((lambda x, y: x * y), 4, 5) # 20

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# out = []
# for i in data :
#     if i % 2 == 0:
#         out.append((i, i ** 2))
# print(out)

# def select(f, col):
#     return [f(x) for x in col]
# def where(f, col):
#     return [x for x in col if f(x)]
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# res = where(lambda x: x % 2 == 0, res)
# print(res) # [2, 8, 38]
# res = list(select(lambda x: (x, x ** 2), res))
# print(res)