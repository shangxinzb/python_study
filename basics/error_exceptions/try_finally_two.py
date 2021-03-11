"""
更复杂的
try...except...else...finally
"""


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is:", result)
    finally:
        # 执行最后的条款？
        print("executing finally clause")


divide(1,2)