"""
日期和时间

Python提供了一个time和calendar模块用于格式化日期和时间
时间间隔是以秒为单位的浮点小数
每个时间戳都已自从1970年1月1日午夜（_划重点_）开始
"""

import time
import calendar

_float_time = time.time()
# 浮点小数，以秒为单位的时间戳
print(_float_time)
# php的time()函数
print(int(time.time()))

# 时间元组
local_time = time.localtime(time.time())
print(local_time)

# 获取格式化的时间
local_time = time.asctime(time.localtime(time.time()))
print(local_time)

# 格式化日期
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化日期转时间戳
_format_time = '2021-3-25 15:39:07'
print(time.mktime(time.strptime(_format_time, "%Y-%m-%d %H:%M:%S")))

# 返回一整年的日历
a = calendar.calendar(2021)
# print(a)

# 返回当前每周起始日期的设置。
print(calendar.firstweekday())

# 是否是闰年
print(calendar.isleap(2021))

# 返回y1,y2之间的闰年总数
print(calendar.leapdays(1993, 2021))

# 返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。
b = calendar.monthcalendar(2021, 3)
print(b)

# 返回指定年月的日历
c = calendar.month(2021, 3)
print(c)