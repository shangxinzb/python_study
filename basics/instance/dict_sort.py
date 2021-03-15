"""
按key或value对字典进行排序
"""

# 声明字典
key_value = {}

# 初始化
key_value[2] = 56
key_value[1] = 2
key_value[5] = 12
key_value[4] = 24
key_value[6] = 18
key_value[3] = 323
key_value[7] = 12

# sorted(key_value) 返回重新排序的列表
# 字典按键排序
print(sorted(key_value))
for k in sorted(key_value):
    print((k, key_value[k]), end=" ")

print()

"""
按value值排序 lambda是匿名函数
"""
print(sorted(key_value.items(), key=lambda kv: (kv[1], kv[0])))

# dict_items([(),(),...])
print(key_value.items())

# lambda 匿名函数，sorted() key = (按value,按key)这种顺序排序
print(sorted(key_value.items(), key=lambda kv: (kv[1], kv[0])))

"""
字典列表排序
"""
lis = [
    {"name": "Taobao", "age": 100},
    {"name": "Runoob", "age": 7},
    {"name": "Google", "age": 100},
    {"name": "Wiki", "age": 200}
]

# 通过age升序排序
print(sorted(lis, key=lambda i: i['age']))

# 通过age降序排序
print(sorted(lis, key=lambda i: i['age'], reverse=True))
