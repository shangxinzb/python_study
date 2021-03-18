"""
mysql 连接
"""


import pymysql

# 打开数据库连接

db = pymysql.connect(host="localhost", user='root', password='root', database='py')

# 使用cursor()方法创建一个游标对象 cursor
cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print(data)