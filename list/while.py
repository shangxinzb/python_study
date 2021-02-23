a, b = 0, 1
while b < 100:
    # print(b)
    a, b = b, a+b


a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b

while False:
    pass #等待键盘中断 Ctrl + C