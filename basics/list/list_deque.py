# 双端队列
from collections import deque


"""
列表作为队列使用
"""


# 遵循先进先出原则
# follow the first in,first out principle

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")

# 从左边出队列
print(queue.popleft())
# 从右边出队列，即正常方式
# exit the queue form the right,which is the normal way
print(queue.pop())

print(queue)


"""
队列推导式
"""


# 创建一个平方列表
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

# 等价于
squares = [x**2 for x in range(10)]
print(squares)

# 创建一个空list
new_list = list()
print(new_list)

# 列表推导式
combs = [(x, y) for x in [1, 2, 3] for y in [1, 2, 3] if x != y]

print(combs)
print(len(combs))

# 等价于
combs = []
for x in [1, 2, 3]:
    for y in [1, 2, 3]:
        if x != y:
            combs.append((x, y))

print(combs)