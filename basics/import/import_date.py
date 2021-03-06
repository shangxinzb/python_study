"""
引入日期模块
"""


import datetime

now = datetime.date.today()
print(now)

# datetime.date只支持年月日，时分秒是不行的
a = datetime.date(2020, 12, 12)
print(a)

b = now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
print(b)

c = now.strftime("%Y-%m-%d")
print(c)

# 日期支持日历算法
birthday = datetime.date(1993, 12, 28)
age = now - birthday
print(age.days)
# 一万天太久，只争朝夕
