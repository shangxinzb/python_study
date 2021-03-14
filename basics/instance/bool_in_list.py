"""
判断元素是否在列表中
"""


list = [*range(1, 10)]
search = 3

# for
for i in list:
    if i == 3:
        print("for: {} in list".format(search))

# in
if search in list:
    print("in: {} in list".format(search))

# set...in 返回一个无序不重复集合
list_set = set(list)
# print(list_set)
if search in list_set:
    print("set...in: {} in list".format(search))

# count
if list.count(search) > 0:
    print("count: {} in list".format(search))

# 清空列表
empty_list = [*range(1, 10)]
print(empty_list)
empty_list.clear()
print(empty_list)

