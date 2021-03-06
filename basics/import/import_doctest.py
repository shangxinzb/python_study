"""
引入测试模块

doctest模块提供了一个工具，扫描模块并根据程序中内嵌的文档字符串执行测试。

测试构造如同简单的将它的输出结果剪切并粘贴到文档字符串中。

通过用户提供的例子，它强化了文档，允许 doctest 模块确认代码的结果是否与文档一致:
"""


def average(values):
    """
    计算一组数字的平均数
    :param values:
    :return:
    这里的意思是在doc里面输出结果，然后指定一个结果，
    执行结果和指定的结果一样时，则为通过
    否则抛出异常
    >>> print(average([20, 30, 40]))
    30.0
    """
    return sum(values) / len(values)


import doctest
# 自动验证嵌入
doctest.testmod()

ava = average([20, 30, 4])
print(ava)