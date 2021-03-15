""""
计算字典值之和
"""


def cumulative(_dict):
    """
    使用for循环累加的方法
    :param _dict:
    :return:
    """
    params_sum = 0
    for k, v in dict_a.items():
        if isinstance(v, (int, float)):
            params_sum += v

    print(params_sum)


def sum_sample_writing(_dict):
    """
    使用sum() 函数的简化写法
    :param _dict:
    :return:
    """
    print(sum([v for k, v in dict_a.items() if isinstance(v, (int, float))]))


if __name__ == '__main__':
    dict_a = {
        'a': 1,
        'b': 2.34,
        'c': '5.1',
        'd': '1a',
        'e': 'b2'
    }

    cumulative(dict_a)
    sum_sample_writing(dict_a)
    