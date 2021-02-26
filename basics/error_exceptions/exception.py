"""
主动抛出一个异常
raise [Exception [, args [, traceback]]] 抛出一个指定的异常
"""

try:
    raise Exception('spam','other', 'burook')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)

    x, y, z = inst.args
    print('x:', x)
    print('y:',y)
    print('z:', z)
    # print('a:', a)

    for ex in inst.args:
        # 打印异常的所有参数
        print('i am args:', ex)

x = 10
if x > 5:
    pass
    # raise Exception('x 不能大于5.x的值为{}'.format(x))

# 抛出异常后，下面的语句将不会在执行
print(213)

try:
    raise NameError("what is your name?")
except NameError:
    print('an exception flew by!')
    raise  # 这句话的意思是再次抛出异常
