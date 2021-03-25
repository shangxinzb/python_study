"""
repr()函数将对象转化为供解释器读取的形式
语法：
repr(obj)
返回值：
返回一个对象的string格式
"""

_str = 'hello'

repr(_str)

_dict = {'today': '2021-3-25 11:52:28', 'temperature': '13℃'}

print(_dict)

a = repr(_dict)
print(a)