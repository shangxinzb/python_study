"""
字符串翻转
"""


str = "interesting"
# 切片
print(str[::-1])

# 使用reversed() 函数返回一个反转的迭代器。
print(''.join(reversed(str)))

for i in reversed(str):
    print(i)


"""
字符串切片及翻转
这个例子实在垃圾，看起来好麻烦
"""
input = "123456"
# 截取两个字符串
cut_num = 2

l_first = input[0:cut_num]
l_second = input[cut_num:]
r_first = input[0:len(input)-cut_num]
r_second = input[len(input)-cut_num:]

print("头部切片翻转 : ", (l_second + l_first))
print("尾部切片翻转 : ", (r_second + r_first))

# print(r_second)
