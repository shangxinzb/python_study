"""
选择排序

选择排序（Selection sort）是一种简单直观的排序算法。
它的工作原理如下。
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
然后，再从剩余未排序元素中继续寻找最小（大）元素，
然后放到已排序序列的末尾。
以此类推，直到所有元素均排序完毕。
"""

import random


def select_sort():
    # 生成一个随机的列表
    _list = [random.randint(1, 100) for _ in range(10)]

    for i in range(len(_list)):
        # 假设最小元素下标为当前值 i
        min_idx = i
        # 从下一个元素下标开始循环
        for k in range(min_idx + 1, len(_list)):
            # 最小数 > 下一个下标数
            if _list[min_idx] > _list[k]:
                # 内容互换
                _list[min_idx], _list[k] = _list[k], _list[min_idx]

    print(_list)


if __name__ == '__main__':
    select_sort()
