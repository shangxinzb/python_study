"""
移除字符串中指定位置字符
"""
# 如果我能像你那么潇洒就好了
test_str = "if only i could be as handsome as you"
# 移除第十个字符
del_character = 10
new_str = ''

"""
使用for循环
"""
for i in range(len(test_str)):
    if i != del_character:
        new_str += test_str[i]

print(new_str)

"""
使用字符串替换
"""
new_str = test_str.replace(test_str[del_character], '', 1)
print(new_str)

"""
使用字符串切片
"""
print(test_str[:del_character] + test_str[del_character + 1:])
