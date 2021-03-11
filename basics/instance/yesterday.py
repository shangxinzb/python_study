"""
获取昨天的日期
"""

import datetime

today = datetime.date.today()
current_datetime = datetime.datetime.now()
one_day = datetime.timedelta(days=1)
yesterday = today - one_day



print(today)
print(current_datetime)
print(one_day)
print(yesterday)