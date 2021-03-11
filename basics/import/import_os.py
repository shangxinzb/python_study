"""
操作系统接口
"""


import os
import math

# 返回当前工作目录
print(os.getcwd())

# 修改当前的工作目录
os.chdir('../')

print(os.getcwd())

# 执行系统命令 mkdir
# os.system('mkdir today')

for i in dir(os):
    # print(i)
    pass

print(len(list(dir(os))))


help(os)

