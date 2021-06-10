# coding=utf-8

# for i in range(1, 1000):
#
#     if i % 2 == 1 and i % 3 == 2 and i % 5 == 4 and i % 6 == 5 and i % 7 == 0:
#         print(i)
#
#         break


# coding=utf-8

# from math import *
#
# h = input()
# f = input()
#
# x = 1 / 2 * int(f) - int(h)
# y = 2 * int(h) - 1 / 2 * int(f)
#
# print('rabbit={},chicken={}'.format(int(x), int(y)))

# coding=utf-8

x = input()
y = 0
x = int(x)
if x >= 10:
    y = 0.5 * 10
    x = x - 10
    y = y + (x * 1)
else:
    y = 0.5 * x

print(round(y, 1))
