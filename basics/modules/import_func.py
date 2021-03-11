# 这样可以导入所有除了下划线(_)开头的命名
from sys import *
# 引入斐波那契数列方法文件
import fib
# 还可以写成,这样可以直接使用fib2调用方法
from fib import fib2

# 调用函数
print(fib.fib2(10))

print(fib.__name__)

# 可以给方法赋值一个本地变量，这个变量相当于xxx.func
current_func_name = fib.fib2

print(current_func_name(20))