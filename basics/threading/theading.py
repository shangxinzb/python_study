"""
threading模块创建线程
直接从threading.Thread继承创建一个新的子类，并实例化猴调用start()方法启动新线程，即它调用了线程的run()方法
"""

import threading
import time

exitFlag = 0

# 括号里是继承一个类,
class myThread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        # 子类继承父类的__init__方法，两种写法都可以
        # threading.Thread.__init__(self)
        super(myThread, self).__init__()
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程：", self.name)
        print_time(self.name, self.counter, 5)
        print("退出线程：", self.name)

def print_time(thread_name, delay, counter):
    while counter:
        if exitFlag:
            thread_name.exit()
        time.sleep(delay)
        print("{0}:{1}".format(thread_name, time.ctime(time.time())))
        counter -= 1

# 创建新线程
thread1 = myThread(1, 'thread_1', 1)
thread2 = myThread(2, 'thread_2', 2)

# 开启新线程
thread1.start()
thread2.start()
print('当前线程变量：', threading.currentThread())
print('正在运行的线程list：', threading.enumerate())
print('正在运行的线程数量：', threading.activeCount())
print("线程名称：", thread1.getName())
print("是否还在活动", thread1.is_alive())
thread1.join()
thread2.join()

print("退出主线程")