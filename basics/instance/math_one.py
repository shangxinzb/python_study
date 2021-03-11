"""
输出指定范围内的素数
"""

lower = 1
upper = 100

for num in range(lower, upper + 1):
    # 素数大于1
    if num > 1:
        for i in range(2, num):
            # 当前数num除以从2开始递增至自身-1的数，如果有可以除尽的。
            # 则跳出本次循环
            if (num % i) == 0:
                break
        else:
            # 没有任何数可以被除尽，则是素数
            print(num)
