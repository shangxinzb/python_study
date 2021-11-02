import requests

url = "https://item.jd.com/10023605369780.html"

try:
    # 定义一个键值对，更改user-agent属性
    kv = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'}
    r = requests.get(url, headers=kv)
    # r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding

    print(r.request.headers)

    print(r.text)
except:
    print('error')
