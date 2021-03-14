"""
将列表中的头尾两个元素对调
"""


def my_self(a_list):
    """
    取得列表的第一个元素和最后一个元素，
    然后互换位置
    :param a_list:
    :return:
    """

    temp = a_list[0]
    a_list[0] = a_list[-1]
    a_list[-1] = temp
    print(a_list)


def answer(a_list):
    """
    x, y = y, x
    :param a_list:
    :return:
    """

    a_list[0], a_list[-1] = a_list[-1], a_list[0]
    print(a_list)


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    # 快速创建一个list * 为解包符号
    list = [*range(1, 10)]
    # print(list)
    # my_self(arr)
    answer(arr)


