list = [1, 2, 3, 4]
it = iter(list)

# 打印迭代器的下一个元素
# print(next(it))
# print(next(it))

# 循环迭代器
# for x in it:
#     print(x, end = "\n")

# next()函数
import sys

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit("退出")
