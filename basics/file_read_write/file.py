# -*- coding: utf-8 -*-
import json
"""
文件读写
"""

# 打开一个文件
# 函数open()返回文件对象，open(filename, mode)
f = open('demo.txt', 'r+', encoding='utf-8')
print(f)

"""
第一个参数是一个含有文件名的字符串。
第二个参数也是一个字符串，含有描述如何使用该文件的几个字符。
mode 为 'r' 时表示只是读取文件；
'w' 表示只是写入文件（已经存在的同名文件将被删掉）；
'a' 表示打开文件进行追加，写入到文件中的任何数据将自动添加到末尾。 
'r+' 表示打开文件进行读取和写入。
mode 参数是可选的，默认为 'r'。
"""

# 读取文件
# 打开文件时，添加encoding='utf-8'解决不显示中文的办法
print(f.read())

# 读取一行文件
print(f)
# 由于上面已经执行过一次f.read()，读取后会关闭文件，需要重新打开文件
f = open('demo.txt', encoding='utf-8')
# 循环遍历文件对象读取文件中的每一行
for line in f:
    """
    end=''的意义是每一行的最后一个字符是''，而不是默认的换行符
    如果没有end='',则返回内容为
    123
    
    english
    
    中文
    """
    print(line, end='')
# 换行
print('\n')


# 把文件中的所有行读到一个列表中，可以使用list(f) 或者 f.readlines()
f = open('demo.txt', encoding='utf-8')
print(list(f))
f = open('demo.txt', encoding='utf-8')
print(f.readlines())

# f.write(string) 方法将string的内容写入文件，并返回字符的长度
f = open('demo.txt', 'a', encoding='utf-8')
print(f.write('append new line.\n'))
print(f.write('append second line.\n'))

# 想要写入其他非字符串内容，首先要将它转换为字符串
value = ('the answer', 42)
s = str(value)
f = open('demo.txt', 'a', encoding='utf-8')
f.write(s)

print(f.tell())

f.close()

#用关键字 with 处理文件对象是个好习惯。它的先进之处在于文件用完后会自动关闭，就算发生异常也没关系。
# 它是 try-finally 块的简写:
print('----------------------------')
with open('demo.txt', 'r', encoding='utf-8') as f:
    print(f.read())
f.close()


# json 数据解析
# python字典类型转换为json对象
data = {
    'date': '2021-2-26 17:21:01',
    'weather': 'sunny',
    'holiday': 'lantern festival'
}

# json_str = json.dumps(data)
# 写入json数据
with open('a.txt', 'a') as f2:
    json.dump(data, f2)
    f2.write('\n') # 换行
f2.close()
# 读取数据 为什么这个报错 ？
# with open('a.txt', 'r') as f3:
#     print(json.load(f3))

# 写入一个json文件
with open('data.json', 'w') as f_json:
    json.dump(data, f_json)
    f_json.close()

# 读取json文件数据
with open('data.json', 'r') as f4:
    print(json.load(f4))