"""
计算元素在列表中出现的次数
"""


import random

list = [random.randint(1, 5) for i in range(10)]
search = 3

"""
list.count()
"""
print("list.count(): {0} count {1} in list".format(search, list.count(search)))

"""
for
"""
count = 0
for elem in list:
    if elem == search:
        count += 1

print("for:{0} count {1} in list".format(search, count))
