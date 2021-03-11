"""
列表操作
join 分割list为字符串
split 将字符串转换为list
"""

# 使用join链接list成为字符串
params = {"server": "mpilgrim", "database": "master", "uid": "sa", "pwd": "secret"}
a = ["%s=%s" % (k, v) for k, v in params.items()]

print(a)

b = ";".join(["%s=%s" % (k, v) for k, v in params.items()])

print(b)

# list 分割字符串
li = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
str = ','.join(li)
print(str)

new_list = str.split(',')
print(new_list)

# list的映射解析
li = [1, 2, 3, 4, 5]
# 生成一个新的list
print([new_element*2 for new_element in li])
# 原list内容不变
print(li)

# dictionary中的解析
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
print(params.keys())
print(params.values())
print(params.items())
# 获取key
list_key = [k for k, v in params.items()]
# 获取value
list_value = [v for k, v in params.items()]

# list 过滤
li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
# 获取字符串长度大于1的
list_greater_than_1 = [k for k in li if len(k) > 1]
print(list_greater_than_1)

# 字符不等于d的
list_not_d = [k for k in li if k != 'd']
print(list_not_d)

# list.count()方法用于统计某个元素在列表中出现的次数
list_count_2 = [k for k in li if li.count(k) == 2]
print(list_count_2)

# 输出一个不重复的元素序列
"""
set()函数是无须不重复的集合
list()将集合转换成列表
"""
print(list(set(list_count_2)))

# list搜索
li = ['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']
# 查找参数new第一次出现的索引下标
new_index = li.index("new")
print(new_index)

# 如果元素不在list中,会报ValueError
# 使用try...except..跑出异常
try:
    error_index = li.index("hello")
    print(error_index)
except ValueError as e:
    print(e)
else:
    print("如果是正确的，终究还是来到了这里。")

# 使用in 判断元素是否在列表中
bool_hello = "hello" in li
print(bool_hello)

# list增加元素
li = ['a', 'b', 'mpilgrim', 'z', 'example']
# li追加一个元素
li.append("cool")

# 在list指定下标增加一个元素
li.insert(3, "english")

# extend()函数用于在列表末尾一次性追加另一个序列中的多个值
list_two = ["computer", 'keyboard']
li.extend(list_two)

print(li)

# list删除元素
li = ['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']
# list删除一个元素，没有返回值
li.remove('z')

# pop() 删除list中的最后一个元素，然后返回删除元素的值
pop_elem = li.pop()

print(pop_elem)