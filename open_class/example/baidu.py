import requests

kv = {'wd': 'python'}

url = "http://www.baidu.com"

r = requests.get(url + "/s", params=kv)

r.encoding = r.apparent_encoding

print(r.status_code)
# 请求的url链接是什么
print(r.request.url)

print(len(r.text))
