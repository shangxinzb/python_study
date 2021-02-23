"""
数据结构 data structure
"""

demo_list = []
# 在列表的末尾添加一个元素
demo_list.append(1)
demo_list.append('jojo')

# 使用可迭代的对象中的所有元素来扩展列表
demo_list.extend((1, 2, 3))

# 在给定的位置插入一个元素。第一个参数是要插入的元素的索引，
# 所以a.insert(0, x) 插入列表头部，a.insert(len(a), x)等同于a.append(x)
# 即在列表的末尾添加一个元素
demo_list.insert(1, 'come on')

# 移除列表中第一个值为x的元素。如果没有这样的元素，则跑出ValueError异常
demo_list.remove(1)

# 删除列表中给定位置的元素并返回它。如果没有给定位置，a.pop()将会删除并返回列表中的最后一个元素。
demo_list.pop(-1)

# 移除列表中的所有元素，等价于del a[:]
# demo_list.clear()

# index() 函数用于从列表中找出某个值第一个匹配项的索引位置。
# 如果没有这样的元素将会抛出ValueError异常。
print(demo_list.index(1))

# 返回元素x在列表中出现的次数
demo_list.append('jojo')
# 元素出现的次数
print('number of occurrences of the element:', demo_list.count('jojo'))

# 对列表中的元素进行排序
# no way to compare strings and numbers
demo_list.remove(1)
demo_list.remove(2)
demo_list.sort()

# 翻转列表中的元素
# x的最后一个元素，变为列表的第一个元素
# the last element x becomes the first element in the list
demo_list.append('ahha')
demo_list.append('youkumaha')

demo_list.reverse()

# 返回列表的一个浅拷贝，等价于a[:]
demo_list2 = demo_list.copy()

print(demo_list)
print(demo_list2)


