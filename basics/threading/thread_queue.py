"""
线程优先级队列 Queue

Queue 模块中的常用方法:
Queue.qsize() 返回队列的大小
Queue.empty() 如果队列为空，返回True,反之False
Queue.full() 如果队列满了，返回True,反之False
Queue.full 与 maxsize 大小对应
Queue.get([block[, timeout]])获取队列，timeout等待时间
Queue.get_nowait() 相当Queue.get(False)
Queue.put(item) 写入队列，timeout等待时间
Queue.put_nowait(item) 相当Queue.put(item, False)
Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
Queue.join() 实际上意味着等到队列为空，再执行别的操作
"""

import queue
import threading
import time

exitFlag = 0


# 注意细节 (=ω=;)
# expected 2 blank lines, found 0
# 预期要有两个空行，目前是0行
# class names should use camelcase convention
# 类名应该使用驼峰格式约定
class MyThread(threading.Thread):
    def __init__(self, _thread_id, _thread_name, _que):
        super(MyThread, self).__init__()
        self.thread_id = _thread_id
        self.thread_name = _thread_name
        self.que = _que

    def run(self):
        """
        class内的方法，每个方法之间只需要一个空行
        :return:
        """
        print('start thread:', self.thread_name)
        # do something
        process_data(self.thread_name, self.que)
        print('end thread:', self.thread_name, end='\n\r')


def process_data(thread_name, que):
    """
    打印进程数据
    :param thread_name:
    :param que:
    :return:
    """
    while not exitFlag:
        # 获取锁
        queue_lock.acquire()
        # 如果队列不为空
        if not work_queue.empty():
            # 获取队列数据
            # 如果是在实际应用中，这个地方应该是处理逻辑的地方吧。
            data = que.get()
            # print(data)
            # 释放锁
            queue_lock.release()
            print("%s processing %s" % (thread_name, data))
        else:
            queue_lock.release()
        time.sleep(1)


# 创建线程名称（列表）
thread_list = ['thread_' + str(i) for i in range(1, 4)]
# 造点数据
name_list = [i for i in range(10)]
# 声明锁？
queue_lock = threading.Lock()
"""
queue.Queue(maxsize = 0) 
如果设置了最大连接数量，一旦填充的数量大于最大连接数，
程序则什么都不输出，也不会走except、finally
"""
work_queue = queue.Queue()
threads = []
thread_id = 1

try:
    # raise RuntimeError("强制返回")
    # assert False, "666"
    # print('继续执行')

    # 创建新线程
    for t_name in thread_list:
        # 实例化线程
        thread = MyThread(thread_id, t_name, work_queue)
        # 开始线程
        thread.start()
        # 加入线程列表
        threads.append(thread)
        thread_id += 1

    # 填充队列
    queue_lock.acquire()
    for word in name_list:
        work_queue.put(word)
    queue_lock.release()

    # 等待队列清空
    while not work_queue.empty():
        pass

    # 通知线程退出
    exitFlag = 1

    # 等待所有线程完成
    for t in threads:
        t.join()

    print("exit thread")
except Exception as e:
    print(e)
finally:
    print("兜底。")
