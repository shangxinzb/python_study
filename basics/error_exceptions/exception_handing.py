"""
首先，执行 try 子句 （在 try 和 except 关键字之间的部分）。

如果没有异常发生， except 子句 在 try 语句执行完毕后就被忽略了。

如果在 try 子句执行过程中发生了异常，那么该子句其余的部分就会被忽略。

如果异常匹配于 except 关键字后面指定的异常类型，就执行对应的except子句。
然后继续执行 try 语句之后的代码。

如果发生了一个异常，在 except 子句中没有与之匹配的分支，它就会传递到上一级 try 语句中。
"""

# 异常处理
while True:
    try:
        x = int(input("please enter a number:"))
        break
    except ValueError:
        print("try again.")