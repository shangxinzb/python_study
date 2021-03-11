"""
try...except...else
另一种尝试
测试else是否是必须执行的流程
"""

for i in range(10):
    try:
        print('i:', i)
        print('i / -1:', i / -1)
    except ValueError:
        print('is error')
    else:
        # 当try语句没有抛出异常的时候，会执行这个方法
        print('the processes that must be performed.')