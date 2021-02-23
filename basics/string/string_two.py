a = b = c = 123

a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a))

# 删除对象引用
# del a

list = ['abcd', 213, 2.32, 'dsad', 3249, 'fas32', 932.3]

tinylist = [213, 'fsdhjj']
print(list)
print(list[0:2])
print(list[2:])
print(tinylist * 2)
print(list + tinylist)

list[0] = '我是传奇'

print(list)

print(list[1::2])

test_str = "都 打发顺丰 死神镰刀 放到 数据库I E我耐 腐蚀"
# 字符串分隔成列表
inputWords = test_str.split(" ")
print(inputWords)
# 字符串翻转
inputWords = inputWords[-1::-1]
print(inputWords)
# 重新组合字符串
output = ' '.join(inputWords)

print(output)
