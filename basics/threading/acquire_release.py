"""
线程同步
简单的锁和释放
"""

import threading
import time


class myThread(threading.Thread):
    def __init__(self, thread_id, thread_name, counter):
        """
        初始化
        :param thread_id: 线程ID（这个id不应该是自己定义的吧？）
        :param thread_name: 线程名称（如果名称重名了怎么办）
        :param counter: 间隔秒数（从代码的角度上来理解）
        """
        super(myThread, self).__init__()
        self.thread_id = thread_id
        self.thread_name = thread_name
        self.counter = counter

    def run(self):
        print("开启线程：", self.thread_name)
        # 获取锁，用于线程同步
        thread_lock.acquire()
        # 一些逻辑处理
        print_time(self.thread_name, self.counter, 3)
        # 释放锁，开启下一个线程
        thread_lock.release()


def print_time(thread_name, delay, counter):
    """
    打印线程名称和线程执行时的时间
    :param thread_name: 线程名称
    :param delay: 延迟时间
    :param counter: 数量
    :return:
    """
    while counter:
        time.sleep(delay)
        print("%s:%s" % (thread_name, time.ctime(time.time())))
        counter -= 1


# 声明一个线程锁？
thread_lock = threading.Lock()
threads = []

# 创建新的线程
thread_1 = myThread(1, 'thread_1', 1)
thread_2 = myThread(2, 'thread_2', 1)
# 开启线程
thread_1.start()
thread_2.start()
# 添加线程到列表
threads.append(thread_1)
threads.append(thread_2)
# 等待所有线程完成
for t in threads:
    t.join()
print("退出主线程")

"""
开启线程： thread_1
开启线程： thread_2
thread_1:Tue Mar 23 21:15:44 2021
thread_1:Tue Mar 23 21:15:45 2021
thread_1:Tue Mar 23 21:15:46 2021
thread_2:Tue Mar 23 21:15:47 2021
thread_2:Tue Mar 23 21:15:48 2021
thread_2:Tue Mar 23 21:15:49 2021
退出主线程
"""
