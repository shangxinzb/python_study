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
        print(left, right)
        middle = int(left + (right - left) / 2)

        print("middle:", middle)
        print("elem:", arr[middle])
        # 正好是要找的值
        if arr[middle] == search:
            return middle
        # 找的值比中间值大
        elif search > arr[middle]:
            # 在右边找
            return binary_search(arr, middle + 1, right, search)
        # 找的值比中间值小
        else:
            # 在左边找
            return binary_search(arr, left, middle - 1, search)
    else:
        # 不存在
        return -1


# 返回 x 在 arr 中的索引，如果不存在返回 -1
def binarySearch(arr, l, r, x):
    # 基本判断
    if r >= l:
        print(l, r)
        mid = int(l + (r - l) / 2)
        print('mid:', mid)
        print('elem:', arr[mid])
        # 元素整好的中间位置
        if arr[mid] == x:
            return mid

            # 元素小于中间位置的元素，只需要再比较左边的元素
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

            # 元素大于中间位置的元素，只需要再比较右边的元素
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # 不存在
        return -1


def again(arr, left, right, search):
    if right >= left:
        # pass
        # 求中间值
        mid_elem = int(left + (right - left) / 2)

        if arr[mid_elem] == search:
            return mid_elem
        elif arr[mid_elem] > search:
            # 在左边
            return again(arr, left, mid_elem - 1, search)
        else:
            # 在右边
            """
            因为arr[mid_elem] ！= search，所以再次查询的时候，left最小值需要+1
            """
            return again(arr, mid_elem + 1, right, search)
    else:
        return -1


if __name__ == '__main__':
    # 测试数组
    arr = [2, 3, 4, 10, 40]
    search = 10

    result = binary_search(arr, 0, len(arr) - 1, search)
    print(result)
    print('------------------')

    # 函数调用
    result = binarySearch(arr, 0, len(arr) - 1, search)
    print(result)

    print('------------------')

    # 函数调用
    result = again(arr, 0, len(arr) - 1, search)
    print(result)
