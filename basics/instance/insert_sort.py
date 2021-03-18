"""
插入排序（英语：Insertion Sort）是一种简单直观的排序算法。
它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
"""

import random


def insert_sort(un_list):
    """
    插入排序
    :param un_list: 无序列表
    :return:
    """
    for i in range(1, len(un_list)):
        # 上一个元素下标
        value = un_list[i]
        k = i - 1
        while k >= 0 and value < un_list[k]:
            # 当前值 = 上一个值
            un_list[k + 1] = un_list[k]
            # 下标减一，然后在对比
            k -= 1
        # k + 1 的意义为while最后一句话减一，在加回来，两个比较数的互换
        un_list[k + 1] = value

    print(un_list)


def insertionSort(arr):
    for i in range(1, len(arr)):
        # 当前值
        key = arr[i]
        # 上一个元素下标
        j = i - 1
        # 下标大于等于0并且上一个值大于当前值
        while j >= 0 and key < arr[j]:
            # 前后互换位置
            arr[j + 1] = arr[j]
            # 在比较上一个元素下标
            j -= 1
        arr[j + 1] = key
    print(arr)


def twice():
    _list = [random.randint(1, 100) for _ in range(10)]

    for i in range(1, len(_list)):
        value = _list[i]
        k = i - 1

        while k >= 0 and value < _list[k]:
            _list[k + 1] = _list[k]
            k -= 1
        _list[k + 1] = value

    print(_list)


if __name__ == '__main__':
    un_list = [random.randint(1, 100) for _ in range(10)]
    insert_sort(un_list)
    insertionSort(un_list)
    twice()