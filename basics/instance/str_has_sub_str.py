"""
判断字符串是否存在子字符串
"""


"""
使用str.find()
"""
str = "how are you"
sub_str = "you"

if str.find(sub_str) == -1:
    print("不存在")
else:
    print("存在")


"""
使用in
"""
if sub_str in str:
    print("存在")
else:
    print("不存在")