import sqlite3
conn=sqlite3.connect('text.db')
cur=conn.cursor() #创建游标
cur.execute('create table song (排名 int,歌名 text,演唱 text)')
cur.close()
conn.close()