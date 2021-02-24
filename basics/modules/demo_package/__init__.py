""""
一个包的初始化
"""

import math


# 格式化字符串format函数从0开始，可以有多个参数，可以指定元素下标，但是不能下标越界
# 参数还可以使用关键字参数，通过参数名来引用
# 越界抛出IndexError错误
print("this is a string format say {1}, is {good}".format('hello', 'world', good='good job'))

print("the value of pi is {0:.3f}.".format(math.pi))
