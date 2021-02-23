"""
文档字符串
"""

def my_function():
    """
    这个方法什么也不做

    然后这是简介内容
    """
    pass


print(not my_function())


def a():
    tax = 213 * 342
    return tax


print(a())


# annotation mean is 注释
# arguments mean is 参数
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations", f.__annotations__)
    print("arguments", ham, eggs)
    return ham + ' and ' + eggs


print(f('spam', 'jojo'))