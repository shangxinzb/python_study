"""
秒表计时
按下回车开始计时，按下Ctrl + C停止计时
PS：Ctrl + c 不能停止脚本运行
"""

import time


def my_self():
    print("按下回车开始计时。")

    input("")

    start_time = time.time()
    print("开始")
    try:
        while True:
            print("计时：", round(time.time() - start_time, 0), "秒")
            time.sleep(1)
    except KeyboardInterrupt:
        print("结束")
        end_time = time.time()
        print("总共的时间为", end_time - start_time, '秒')
    except BaseException as e:
        print("进来了")
        if isinstance(e, KeyboardInterrupt):
            print("结束")


def answer():
    print('按下回车开始计时，按下 Ctrl + C 停止计时。')
    while True:
        input("")  # 如果是 python 2.x 版本请使用 raw_input()
        starting = time.time()
        print('开始')
        try:
            while True:
                print('计时: ', round(time.time() - starting, 0), '秒')
                time.sleep(1)
        except KeyboardInterrupt:
            print('结束')
            entire = time.time()
            print('总共的时间为:', round(entire - starting, 2), 'secs')
            break
        else:
            print("what?")


def always_while():
    i = 1
    while True:
        print(i)
        i += 1


if __name__ == '__main__':
    # answer()
    my_self()
    # always_while()


