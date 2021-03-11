"""
访问互联网网页
使用urlopen打开一个网页，将每行信息循环输出
选择匹配的内容打印
"""


from urllib.request import urlopen


for line in urlopen('http://www.baidu.com/'):
    line = line.decode('utf-8')
    if '2021' in line or 'EDT' in line:
        print(line)