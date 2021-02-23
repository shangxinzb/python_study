"""
集合
"""


# Python也包含有 集合 类型。集合是由不重复元素组成的无序的集。它的基本用法包括成员检测和消除重复元素。
# 集合对象也支持像 联合，交集，差集，对称差分等数学运算。
# 花括号或 set() 函数可以用来创建集合。注意：要创建一个空集合你只能用 set() 而不能用 {}，因为后者是创建一个空字典，
# basket 篮子
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print('apple' in basket)

# 演示两个单词的唯一字母的集合操作
a = set('dakdfasddsadf')
b= set('hjfdsdfdhjdskj')

# 集合的内容会被去重
print(a)
print(b)

# 在a集合中的字符但是不在b集合中
print(a - b)
# 在a集合或者在b集合中
print(a | b)
# 在a集合并且在b集合中
print(a & b)
# 在a集合或者b集合，但不是都有
print(a ^ b)