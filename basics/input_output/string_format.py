"""
字符串格式化输出
"""


import math


# 格式化字符串format函数从0开始，可以有多个参数，可以指定元素下标，但是不能下标越界
# 参数还可以使用关键字参数，通过参数名来引用
# 越界抛出IndexError错误
print("this is a string format say {1}, is {good}".format('hello', 'world', good='good job'))

print("the value of pi is {0:.3f}.".format(math.pi))

# 如果你有个实在是很长的格式化字符串，不想分割它。如果你可以用命名来引用被格式化的变量而不是位置就好了。
# 有个简单的方法，可以传入一个字典，用中括号( '[]' )访问它的键
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))

# 也可以用 ‘**’ 标志将这个字典以关键字参数的方式传入:
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))