"""
数组翻转指定个数的元素

定义一个整型数组，并将指定个数的元素翻转到数组的尾部。
例如：(ar[], d, n) 将长度为 n 的 数组 arr 的前面 d 个元素翻转到数组尾部。
"""


def my_self(arr, flip_num):
    """
    使用数组翻转，使用pop删除flip_num个元素
    在将删除的元素添加到数组的最后
    """
    # print(arr[:flip_num])
    # 列表切片赋值，不影响原list
    calculate_arr = arr[:]
    # 数组翻转
    calculate_arr.reverse()
    print(arr)

    for _ in range(flip_num):
        elem = calculate_arr.pop()
        # print(elem)
        arr.remove(elem)
        arr.append(elem)

    print(arr)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    my_self(arr, 2)
