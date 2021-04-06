import pymysql

conn = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='edu')
cursor = conn.cursor()
cursor.execute('select * from dsc_users')
print(cursor.fetchone())