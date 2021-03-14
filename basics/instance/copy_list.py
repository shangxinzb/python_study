"""
复制列表
"""

import random


# 搞一个随机的列表
main_list = [random.randint(1, 100) for i in range(10)]
# print(main_list)


def print_result(main_list, copy_list):
    copy_list.append(1)
    print("main_list:", main_list)
    print("copy_list:", copy_list)


"""
切片复制
"""
copy_list = list()
copy_list = main_list[:]
print_result(main_list, copy_list)

"""
继承复制
"""
copy_list = list()
copy_list.extend(main_list)
print_result(main_list, copy_list)

"""
list()声明
"""
copy_list = list()
copy_list = list(main_list)
print_result(main_list, copy_list)


"""
list.copy()
"""
copy_list = list()
copy_list = main_list.copy()
print_result(main_list, copy_list)

"""
=指向
"""
copy_list = list()
copy_list = main_list
# 原数组同样变化
print_result(main_list, copy_list)

