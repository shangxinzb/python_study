import math

"""
字典
"""


# dict()构造函数可以直接从键值对序列里创建字典
some_dict = dict([('sape',2131), ('guidiao', "324324")])
# 直接用花括号创建字典
some_dict = {'das': 231, 'aaa': 'fdsfsd'}
print(some_dict)

# 字典推导式可以从任意的键值表达式中创建字典
a_dict = {x: x**2 for x in range(2, 10, 2)}

print(a_dict)

# 关键字是简单字符串时，可以直接通过关键字参数来制定键值对
b_dict = dict(dsajkd=2314, fdskjf=342, fdsfs='fdsfs')

print(b_dict)


# 循环技巧
# 在字典循环中，用items()方法可以将关键字和对应的值同时取出
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# 在列表中循环时，用enumerate()函数可以将索引位置和其对应的值同时取出
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# 当同时在两个或更多序列中循环时，可以用zip()函数将其元素一一匹配
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print("What is your {0}? It is {1}".format(q, a))

# 如果要逆向循环一个序列，首先正向定位序列，然后调用reversed()函数
for i in reversed(range(2, 10, 2)):
    print(i)

# 如果要按某个指定顺序循环一个序列，可以用哪个sorted()函数，它可以在
# 不改动原序列的基础上返回一个新的排好序的序列
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

print(set(basket))
print(sorted(set(basket)))
print(sorted(basket))
print(basket)

# 有时可能会想在循环时修改列表内容，一般来说改为创建一个新列表是比较简单且安全的
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
# 数组使用enumerate()函数可以拆分为k, v模式
for k, value in enumerate(raw_data):
    print('k,v:', k, value)
    # if not math.isnan(value):
    #     filtered_data.append(value)

# print(filtered_data)

a = 1
b = 2

