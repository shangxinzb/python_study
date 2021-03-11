"""
九九乘法表
横向输出内容
"""

for i in range(1, 10):
    for k in range(1, i + 1):
        print("{0}*{1}={2}\t".format(k, i, i * k), end='')
    print()  # 打印完一行数据进行换行操作
