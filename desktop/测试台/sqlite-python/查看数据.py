import sqlite3
conn=sqlite3.connect('text.db')
cur=conn.cursor() #创建游标
cur.execute('SELECT*FROM 信息表 WHERE 姓名="张三"')
data=cur.fetchall()
print(data)
cur.close()
conn.close()