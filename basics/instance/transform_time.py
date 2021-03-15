"""
字符串转换为时间戳
"""


import time


_a = "2021-3-15 18:49:20"
# 先转换为时间数组
time_arr = time.strptime(_a, "%Y-%m-%d %H:%M:%S")

# 转换为时间戳
time_stamp = int(time.mktime(time_arr))
print(time_stamp)

# 转换格式
_a_2 = "2021-3-15 18:51:46"
# 转换为其他格式，现将时间字符串转换为时间数组
# 然后在转换为其他格式
time_arr = time.strptime(_a_2, "%Y-%m-%d %H:%M:%S")
# 格式化日期
new_time = time.strftime("%Y/%m/%d %H:%M:%S", time_arr)
print(new_time)

"""
获取几天前的时间
"""

import datetime


# 先获得时间数组格式日期
three_day_ago = datetime.datetime.now() - datetime.timedelta(days=3)
# 转换为时间戳
# 获取时间数组
time_tup = three_day_ago.timetuple()
# 获取时间戳 因为time.mktime返回一个带小数的时间戳，所以要转换成int
time_stamp = int(time.mktime(time_tup))
print(time_stamp)
# 格式化日期
time_str = three_day_ago.strftime("%Y/%m/%d %H:%M:%S")
print(time_str)
# 一个格式化日期转换为另一个格式化日期
# b = time.strftime("2021-3-15 19:08:47", "%Y/%m/%d %H:%M:%S")
# print(b)

"""
时间戳转换为指定格式的日期
"""
# 这是时间戳
print(time.time())
# 这是格式化日期带小数
print(datetime.datetime.now())

"""
str类型的日期转换为时间戳
"""
str_time = "2021-3-15 19:13:46"
# 字符串转换为时间数组
time_arr = time.strptime(str_time,"%Y-%m-%d %H:%M:%S")
# 转换为时间戳
time_stamp = int(time.mktime(time_arr))
print(time_stamp)


"""
更改str类型日期显示格式
"""
str_time = "2021年3月15日19:16:48"
# 依旧是字符串先转成时间数组
time_arr = time.strptime(str_time, "%Y年%m月%d日%H:%M:%S")
# 转换为其他格式显示
str_time = time.strftime("%Y-%m-%d %H:%M:%S", time_arr)

print(str_time)


"""
时间戳转指定格式日期
"""
# 使用time
# 时间戳
time_stamp = int(time.time())
# 时间戳转换成时间数组
time_arr = time.localtime(time_stamp)
# 转换为格式化日期
time_str = time.strftime("%Y-%m-%d %H:%M:%S", time_arr)


# 使用datetime
# 时间戳
time_stamp = int(time.time())
# 这是返回一个格式化时间字符串
time_str = datetime.datetime.fromtimestamp(time_stamp)
otherStyleTime = time_str.strftime("%Y--%m--%d %H:%M:%S")
print(otherStyleTime)

# print(time_str)