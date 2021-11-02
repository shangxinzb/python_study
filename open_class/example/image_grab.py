import requests
import os

url = "https://hoteledutest.wonmore.com/themes/ecmoban_dsc2017/img/icon/img1.jpg"
root = "E:/code/python_study/open_class/example/"

path = root + url.split('/')[-1]

# print(path)

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("file save success")
    else:
        print('file is exists')
except:
    print('error')
