"""
合并字典
*args将传入的参数转换成一个元组tuple() 解包
**kwargs 关键字参数，将参数转换成一个dict
两个参数同时使用是，*args要写在**kwargs之前
"""


def foo(*args, **kwargs):
    """
    一个简单的例子
    :param args:
    :param kwargs:
    :return:
    """
    print("args", args)
    print("kwargs", kwargs)


def merge(dict_1, dict_2):
    """
    两个字典合并
    :param dict_1:
    :param dict_2:
    :return:
    """
    new_dict = dict_1.update(dict_2)
    return new_dict


def use_kv(dict_1, dict_2):
    """
    使用**,将参数以字典形式导入
    :param dict_1:
    :param dict_2:
    :return:
    """
    print(dict_1)
    print({key:value for key, value in dict_1.items()})
    print({**dict_1, **dict_2})
    print()


if __name__ == '__main__':
    """
    当__name__写在方法之前时，IDE获取不到方法名
    """
    # pass
    dict_1 = {'a': 1, 'b': 2, 'c': 3}
    dict_2 = {'d': 4, 'e': 5, 'f': 6}
    # merge()方法不返回内容，改变的是字典的内容
    print(merge(dict_1, dict_2))
    print(dict_1)

    dict_1 = {'a': 1, 'b': 2, 'c': 3}
    dict_2 = {'d': 4, 'e': 5, 'f': 6}
    use_kv(dict_1, dict_2)