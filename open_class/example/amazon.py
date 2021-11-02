import requests

url = "https://www.amazon.cn/dp/0735355290/ref=sr_1_4?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&dchild=1&keywords=%E5%9B%BE%E4%B9%A6&qid=1623987972&s=amazon-global-store&sr=8-4&srs=1756067071"

try:
    r = requests.get(url)
    print(r.status_code)
    print(r.encoding)
    print(r.request.headers)
    # print(r.text)
except:
    print('error')