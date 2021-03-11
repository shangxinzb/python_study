"""
作为脚本来执行模块
"""

import sys
from fib import fib


if __name__ == "__main__":
    """
    作为脚本执行的时候，可以在执行脚本后面追加参数
    参数使用空格作为分隔
    
    """
    # 打印参数
    for i in sys.argv:
        print(i)
    # fib(int(sys.argv[1]))
    # sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表
    # print("python path is ", sys.path)
