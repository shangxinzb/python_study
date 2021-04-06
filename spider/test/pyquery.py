from pyquery import PyQuery as pq

doc = pq('<html>hello</html>')
# 打印标签里面的内容
result = doc('html').text()
print(result)