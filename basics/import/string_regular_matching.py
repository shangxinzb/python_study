"""
字符串正则匹配
"""


import re


result = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(result)

result = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the hat')
print(result)


# 字符串替换
str_one = 'tea for too'.replace('too', 'two')
print(str_one)