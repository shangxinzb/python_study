"""
抛出一个自定义的异常
创建一个新的异常类来拥有自己的异常，异常类继承自Exception类，
可以直接继承或者间接继承
"""


class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        # repr()函数将对象转化为供解释器读取的形式
        return repr(self.value)


try:
    raise MyError(2*2)
except MyError as e:
    print("my exception occurred, value:", e.value)

print('go on')

try:
    raise MyError("oops!")
except MyError as e:
    print("my exception occurred, value:", e.value)
# raise MyError("oops!")