from turtle import *


# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# 
# clear()
#
# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         color(c)
#         forward(steps)
#         right(30)
#
# clear()

while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break