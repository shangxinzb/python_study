"""
文件IO
"""

# 写文件
with open("test.txt", "wt", encoding='utf-8') as out_file:
    out_file.write("你过来啊！")

# 读取文件
with open("test.txt", "rt", encoding='utf-8') as in_file:
    text = in_file.read()

print(text)