import requests

a = requests.get("http://www.baidu.com")

# 打印请求状态
print(a.status_code)

# 查看header中猜测响应内容编码方式
print(a.encoding)
# 从内容中分析出响应内容中的编码方式
print(a.apparent_encoding)

# 设置编码格式 utf-8
a.encoding = 'utf-8'
print(a.text)

# 查看返回类型
print(type(a))

# header头部信息
print(a.headers)

# http响应内容的二进制形式
print(a.content)

