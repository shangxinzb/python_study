"""
bool()函数用于将给定参数转换为布尔类型，如果没有参数返回false

语法：
class bool([x])
"""

# 空的bool()函数返回false
print(bool())

print(bool(0))

print(bool(None))

print(bool(1))

print(bool(False))

print(bool((1, 2, 3,)))  # true

print(bool([False]))  # true

# 空列表
print(bool([]))  # false

# 元组有一个参数，即使这个参数为0，也返回true
print(bool((0,)))  # true

# 空元组
print(bool(tuple()))  # false

# 空元组
print(bool(()))  # false

# 空字典
print(bool({}))  # false

# bool是int的子类
print(issubclass(bool, int))  # true
