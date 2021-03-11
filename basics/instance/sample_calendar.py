"""
日历
"""

# 引入日历模块
import calendar

# 输入指定年月
yy = int(input("输入年份: "))
mm = int(input("输入月份: "))

# 显示日历
print(calendar.month(yy, mm))

# 计算每个月的天数
"""
输出的是一个元组，第一个元素是查询月份第一天对应的是星期几（0-6）
第二个元素是这个月的天数
"""
month_range = calendar.monthrange(yy, mm)
print(month_range)