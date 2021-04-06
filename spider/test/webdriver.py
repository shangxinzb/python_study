from selenium import webdriver

# 声明一个google浏览器
chrome = webdriver.Chrome()
# 打开百度
chrome.get('http://www.baidu.com')
# 查看网页源代码
print(chrome.page_source)
