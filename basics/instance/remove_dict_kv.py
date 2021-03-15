"""
移除字典键值对
"""

test_dict = {"Runoob": 1, "Google": 2, "Taobao": 3, "Zhihu": 4}

print(test_dict)
print(str(test_dict))

# 删除字典kv
del test_dict['Runoob']

print(test_dict)

try:
    del test_dict['a']
    print(test_dict)
except KeyError as e:
    print(e, "不是一个key")

"""
使用pop移除没有的key不会发生异常，可以自定义提示信息
"""
removed_kv = test_dict.pop("Zhihu")

print(removed_kv)
print(test_dict)

removed_kv = test_dict.pop("Zhihu", '没有key')
print(removed_kv)

"""
使用items()移除
将内容赋值到一个新的字典中
"""
new_dict = {}
for key, value in test_dict.items():
    if key != "Zhihu":
        new_dict[key] = value

print(new_dict)

print({key: val for key, val in test_dict.items() if key != "Zhihu"})
