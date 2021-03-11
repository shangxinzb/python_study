# -*- coding: UTF-8 -*-

"""
平方根使用
"""

num = 5
# 会报类型错误 TypeError:can't convert complex to float
# 不能将复杂类型转换为float类型
# num = -5
num_sqrt = num ** 0.5

print("%0.3f 的平方根为 %0.3f" % (num, num_sqrt))


"""
计算实数和复数的平方根
导入复数数学模块
"""


import cmath


num = -8
num_sqrt = cmath.sqrt(num)

print("{0} 的平方根为 {1:0.3f}+{2:0.3f}j".format(num, num_sqrt.real, num_sqrt.imag))