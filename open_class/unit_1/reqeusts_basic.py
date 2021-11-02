import requests

# Requests库入门
requests.request()
requests.get()
requests.head()
requests.post()
requests.put()
requests.patch()
requests.delete()

# 经常使用get
requests.get()

# 比较大的网页，使用head方法获取资源概要
requests.head()


def get_website(url):
    try:
        r = requests.get(url, timeout=30)
        # 验证返回状态是否是200
        r.raise_for_status()
        # 编码格式改为返回文件内容编码
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "exception"
