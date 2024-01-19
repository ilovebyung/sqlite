import sqlite3
import util
import datetime
import util

conn = sqlite3.connect('sqlite.db')
cursor = conn.cursor()
sql = ('create table tb (date text , time text) ')
conn.execute(sql)

sql = ('create index idx_date on tb (date)')
conn.execute(sql)

date = util.get_date_in_yyyymmdd()
time = util.get_time_in_mmddss()
sql = (f"insert into tb values ({date}, {time})")
conn.execute(sql)
conn.commit()
cursor.close()

cursor = conn.cursor()
cursor.execute("select * from tb")
rows = cursor.fetchall()
for row in rows:
    print(row) 
cursor.close()


'''
always do cursor.close() as soon as possible after having done a (even read-only) query.
'''

# Situations Where SQLite Works Well
#    https://www.sqlite.org/whentouse.html
#    https://www.sqlitetutorial.net/


sql = (f"drop table tb")
conn.execute(sql)
conn.commit()
conn.close()