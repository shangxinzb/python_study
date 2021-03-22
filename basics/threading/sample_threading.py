"""
简单的线程应用
"""

import _thread
import time


def print_time(thread_name, delay):
    """
    定义一个线程函数
    :param thread_name: 线程名称
    :param delay: 延迟
    :return:
    """
    count = 0
    while count <= 5:
        time.sleep(delay)
        count += 1
        print("{0}:{1}".format(thread_name, time.ctime(time.time())))


# 创建两个线程
try:
    _thread.start_new_thread(print_time, ('thread_1', 2,))
    _thread.start_new_thread(print_time, ('thread_2', 5,))
except:
    print("error")

# 监听?
while 1:
    pass