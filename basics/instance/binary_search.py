"""
二分查找

二分搜索是一种在有序数组中查找某一特定元素的搜索算法。
搜索过程从数组的中间元素开始，如果中间元素正好是要查找的元素，
则搜索过程结束；如果某一特定元素大于或者小于中间元素，
则在数组大于或小于中间元素的那一半中查找，
而且跟开始一样从中间元素开始比较。如果在某一步骤数组为空，则代表找不到。
这种搜索算法每一次比较都使搜索范围缩小一半
"""


def binary_search(arr, left, right, search):
    # 数据正常
    if right >= left:
        # pass
        # 找到中间值
        middle = left + int(right - left) / 2

        # 正好是要找的值
        if arr[middle] == search:
            return middle
        # 找的值比中间值大
        elif search > arr[middle]:
            # 在右边找
            binary_search(arr, middle + 1, right, search)
        # 找的值比中间值小
        elif search < arr[middle]:
            # 在左边找
            binary_search(arr, left, middle -1, search)
    else:
        # 不存在
        return -1